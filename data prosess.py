from calendar import day_abbr
from dataclasses import dataclass
from tokenize import String
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas_datareader.data as web
import time

import seaborn as sns
from tqdm import tqdm
from datetime import datetime
import datetime
import re
import holidays
import pickle

dataset = pd.read_csv("C:/Users/xl/Desktop/NLP_LSTM/us_equities_news_dataset.csv")
#dataset = pd.read_excel("C:/Users/xl/Desktop/NLP_LSTM/us_equities_news_dataset.xlsx")
#dataset = pd.DataFrame(dataset)
dataset.drop(inplace=True, columns=['category', 'provider', 'url', 'article_id'], axis=1)
dataset.dropna(inplace = True)
#dataset.info()
dataset.isnull().sum()
#t=dataset.shape[0]

print(dataset[['ticker','release_date']].groupby(['ticker']).count())

#dataset['release_date'] = dataset['release_date'].str.replace('-', '')
#dataset['release_date'] = pd.to_datetime(dataset['release_date'], format='%Y-%m-%d')
dataset.insert(loc=4,column='open',value=0)
dataset.insert(loc=5,column='close',value=0)

#dataset.info()

#print(dataset.index)
ONE_DAY = datetime.timedelta(days=1)
HOLIDAYS_US = holidays.US()
def next_business_day(dateString):
    datetimeObj = datetime.datetime.strptime(dateString, '%Y-%m-%d')
    next_day = datetimeObj + ONE_DAY
    while next_day.weekday() in holidays.WEEKEND or next_day in HOLIDAYS_US:
        next_day += ONE_DAY
    return next_day

for i in range(0,10):
    symble=dataset.iloc[i,1]
    st=dataset.iloc[i,6]
    ed=next_business_day(st).strftime("%Y-%m-%d")
    hist = web.DataReader(symble, 'yahoo', start=st, end=ed)
    last=hist.shape[0]-1
    dataset.iloc[i,4]=hist.iloc[0,2]
    dataset.iloc[i,5]=hist.iloc[last,3]
    print(i)
    #socket.setdefaulttimeout(t)
    time.sleep(0.1)

dataset.to_csv("C:/Users/xl/Desktop/NLP_LSTM/price_result.csv", index=False)



#dataset["ticker"].value_counts().plot(kind="bar")
#plt.show()

#print(dataset['ticker'].unique())
#print(dataset['release_date'].unique())

#print(dataset[['ticker','release_date']].groupby(['ticker']).count())
#[802 rows x 1 columns]

#print(dataset[['ticker','release_date','id']].groupby(['ticker','release_date']).count())
#[120197 rows x 1 columns]

#ticket_count = dataset[['ticker','release_date','id']].groupby(['ticker','release_date']).count()
#sns.barplot(data=ticket_count,x="ticker",y="count",hue="release_date")

#print(dataset.set_index(['ticker']))

#Define the stock ticker dictionary

#tic_date = dataset.groupby(['ticker'])
#count_ticker = dataset['ticker'].nunique()

