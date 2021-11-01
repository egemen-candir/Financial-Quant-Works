import xlwings as xw
import time, datetime
import pandas as pd
import copy
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns


#location of the source file
user_profile = os.environ['USERPROFILE']
user_algofolder = user_profile + "\Documents\Algo"

#read using xlWings
sheet = xw.Book(r''+user_algofolder+ '\XUSIN_Live_Foreks.xlsx').sheets['LiveStocks']

#define interval, number of rolling windows and iterations
#intervals in seconds. Ex: 10 sec inteval with 30 iterations will get 300 secs, ie, 5 mins data
#windows should be less than interval. Ex: In a 10 sec interval, windows of 4 will net two moving averages
interval = 10
windows = 4
iter_times = 10

price_dict = {}

#get the data from Excel and populate an empty dictionary
def mavCount(interval, windows, iterations):
    #take a screenshot of the excel values, record into a dictionary
    for i in range(iterations):
        
        tn = datetime.datetime.now() + datetime.timedelta(seconds=interval)
       
        while datetime.datetime.now()<tn:
            data = sheet["B1"].options(expand= 'table').value
    
            key_name = datetime.datetime.now().strftime("%b-%d, %n %H:%M:%S")
            price_dict[key_name] = copy.deepcopy(data)
            print(price_dict.keys())
            time.sleep(interval)
        
    print(i)
    
    #convert dic to df and clean, format
    
    df = pd.concat({k: pd.DataFrame(v) for k, v in price_dict.items()}, axis=0).reset_index()
    df = df[df.level_1 != 0]
    df = df.rename(columns={'level_0' : 'Date', 0 : 'Ticker', 1 : 'Last'}).set_index('Date')
    df = df.drop(df.columns[3:], axis=1)
    df = df.drop(['level_1'], axis=1)
    df['Last'] = df['Last'].apply(pd.to_numeric, downcast='float', errors='coerce')
    df = df.dropna(axis=0)
    
    #get the rolling moving average of prices and count differences
    df_mav = df.groupby('Ticker').rolling(window=windows).mean()
    mav_count = pd.DataFrame((df_mav['Last'].diff() > 0)).select_dtypes(include=['bool']).sum(axis=1).to_frame().rename(columns={0:'MAV Count'})
    df_delta = pd.DataFrame(mav_count.groupby('Ticker')['MAV Count'].cumsum()).reset_index()
    df_delta.set_index('Date')
    df_final = df_delta.pivot(index='Date', columns='Ticker', values='MAV Count').reset_index()
    df_final = df_final.set_index('Date').T
    df_final = df_final.iloc[: , windows:]
    
    return df_final

df_final =mavCount(interval, windows, iter_times)

#Simple heatmap to illustrate which stock has better momentum
fig, ax = plt.subplots(figsize=(11, 9))
sns.heatmap(df_final, cmap='YlGnBu').set(title='Stock Momentum Heatmap')
plt.show()











