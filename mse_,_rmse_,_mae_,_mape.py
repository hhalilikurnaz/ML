# -*- coding: utf-8 -*-
"""mse , rmse , mae , mape.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZWb7ACswta7gyqrKId945V_iWk1SHtG4
"""

# MSE RMSE MAE MAPE HATALARI
#Mesela ben içinde çeşitli verilerin olduğu bir grafik aldım 2 boyutlu.Bu noktaların arasından regresyon çizgimi çektim.Her nokta bu çizgiyi kesmiyor.kesmeyen noktaların regreson çizgisine uzaklığına hata diyoruz.
#mape mean abstract error

import numpy as np ; import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,mean_absolute_percentage_error

df =pd.read_csv('sigorta.csv')
df.head(3)

#öncelikle kategorisel veriler var bunları dummy ederek numeric verilere çevirmem gerekiyor
df_dummies=pd.get_dummies(df,columns=['sex','smoker','region'],drop_first=True)
df_dummies=df_dummies.astype(int)
df_dummies.head(3)

y=df_dummies['charges']
x=df_dummies.drop('charges',axis=1)

lm=LinearRegression()
model=lm.fit(x,y)

#doğruluk olasılığı
model.score(x,y)

#tahminde bulunuyoruz burada kendimizin verdiği değerlerle
model.predict([[19,26,0,1,1,0,0,1]])

df_hata=pd.DataFrame()

df_hata['y']=y
df_hata

#limdeki bütün x leri verip y'yi tahimin etmesini istiyorum
y_tahmin=model.predict(x)

#şuan veri tablosunda gerçekteki değerler ve tahmin ettiğim değerler var
df_hata['tahmin']=y_tahmin
df_hata

df_hata['error']=y-y_tahmin
df_hata.head(3)

#MSE Mean Square Error hata karaler ortalaması demek
df_hata['square_error']=df_hata['error']**2
df_hata

df_hata['abs_error']=np.abs(df_hata['error'])
df_hata

df_hata['percent_error']=np.abs((y-y_tahmin)/y)
df_hata.head(6)

df_hata.mean()

#burada kütüphaneleri ekleyip direkt olarak fonksiyon şeklinde kullandık easyyyyy
mean_squared_error(y,y_tahmin)