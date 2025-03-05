# -*- coding: utf-8 -*-
"""FBProphet ile Zamana Bağlı Yapay Zeka Tahminler Bitcoin,Google,Dolar Hisse.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nWC2znG-Ma6ziiMEZf3-nVT9EW2DQbE6
"""

#Zamana Bağlı Verilerin Tahminlerini Yapma
#FaceBook Prophet sklearn üzerinden kütüphane finansal verileri kullancağız

import pandas as pd;import numpy  as np
!pip install fbprophet
#bunlar gömülü kütüphane değil yüklememiz lazım

!pip install yfinance

from prophet import Prophet
import yfinance as yf
#yf ise yahoofinance

df=yf.download('BTC-USD',"2019-01-01","2024-09-10")
df.head(3)
df.tail(4)

df=df[['Close']]
df.head(3)

df=df.reset_index()
df.head(3)
#sutun haline getirdi

df.columns=['ds','y']
df.head(3)
#

#Modelimi oluşturdum
model=Prophet()
model.fit(df)

#Ben eğer 100 gün sonrasını tahmin ediceksem 99.cu günü de tahmin etmem lazım.Bir sönceki günü hep tahmin etmem lazım.Bunun DataFrame'ini oluşturuyorum
gelecek=model.make_future_dataframe(360)

tahmin=model.predict(gelecek)

model.plot(tahmin);

model.plot_components(tahmin)

#ARMA , LSTM