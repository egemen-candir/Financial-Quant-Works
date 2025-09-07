import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
import scipy.stats as stats
import dtw
from dtw import dtw,accelerated_dtw

figure(num=None, figsize=(12,12), dpi=200)
df = pd.read_excel(r'TCMBvsUSDTRY.xlsx')

d1 = df['USDTRY Chg'].interpolate().values
d2 = df['Rate Chg'].interpolate().values
d, cost_matrix, acc_cost_matrix, path = accelerated_dtw(d1,d2, dist='euclidean')

plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
plt.plot(path[0], path[1], 'w')
plt.xlabel('USDTRY Change', fontsize=18)
plt.ylabel('TCMB Rate Change', fontsize=18)
plt.title(f'DTW Minimum Path with minimum distance: {np.round(d,2)}', fontsize=18)
plt.show()