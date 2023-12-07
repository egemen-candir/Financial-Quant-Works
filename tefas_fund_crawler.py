# -*- coding: utf-8 -*-
"""TEFAS Fund Crawler.ipynb

Automatically generated by Colaboratory.

"""

from tefas import Crawler
import pandas as pd
import datetime


startDate = datetime.date(2020, 9, 1)
endDate = datetime.date(2023, 11, 11)

tefas = Crawler()
funds = ["KIE","KID","KIF","THD","KIA","KIB","ICF","ICD","ICC"]
f_cols = ["code","date","price","market_cap"]

df = pd.DataFrame()
f_list = []

while startDate <= endDate:
    b_date = startDate.strftime("%Y-%m-%d")
    e_date = (startDate + datetime.timedelta(days=30)).strftime("%Y-%m-%d")
    for f_name in funds:
      t_data = tefas.fetch(start=b_date, end=e_date, name=f_name, columns=f_cols)
      f_list.append(t_data)

    print(b_date,e_date)
    startDate += addDays

df = pd.concat(f_list)
df.sort_values(["code","date"], inplace=True)
df.set_index("code", inplace=True)
df.to_excel("TEFAS_Fonlar.xlsx")

df["Returns"] = df.groupby(["code"])["price"].pct_change()

df.head()

