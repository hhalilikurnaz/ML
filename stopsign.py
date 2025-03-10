# -*- coding: utf-8 -*-
"""stopsign.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jtig5TRlz9xc9zqw8QViPJaq6exDSjbm
"""

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
from sklearn.model_selection import train_test_split

from google.colab import drive
drive.mount('/content/drive')

dataset_path="/content/drive/MyDrive/stop_sign"
dataset_path_nonstops="/content/drive/MyDrive/not_stop"
print(" Klasördeki dosyalar:", os.listdir(dataset_path)[:10])

#  Resimleri 64x64 piksele küçülteceğiz
img_size = 64

#  Boş listeler oluştur (X = Görseller, y = Etiketler)
X = []
y = []

#  Klasördeki her resmi işle
for img_name in os.listdir(dataset_path):
    img_path = os.path.join(dataset_path, img_name)  # Görselin tam yolunu oluştur

    #  Görseli oku
    img = cv2.imread(img_path)

    # Eğer resim okunamazsa hata ver ve geç
    if img is None:
        print(f"{img_path} okunamadı! Geçiliyor...")
        continue

    #  Görseli 64x64 boyutuna getir

    img=cv2.resize(img,(64,64))


    img=img/255.0 #Normalizasyon: 0-255 arasındaki piksel değerlerini 0-1 arasına çevir

    X.append(img)  #  Görselleri X listesine ekle
    y.append(0)  #  Stop işaretleri için etiket = 1

from sklearn.model_selection import train_test_split

X=np.array(X)
y=np.array(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=43)
print(f" Eğitim veri seti boyutu: {X_train.shape}")
print(f" Test veri seti boyutu: {X_test.shape}")

#  Eğitim setinden ilk görseli göster
plt.imshow(X_train[0])
plt.title("Örnek Dur İşareti Görseli")
plt.show()

!pip install tensorflow keras

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout

#Modeli Oluştur
model=Sequential([
    #ilk evrişim Convolution katmanı (32 filtre 3x3 kernal boyutu)
    Conv2D(32,(3,3),activation='relu',input_shape=(64,64,3)),
    MaxPooling2D(pool_size=(2,2)),


    #2.ci evrişim katmanı

    Conv2D(64,(3,3),activation='relu'),
    MaxPooling2D(pool_size=(2,2)),


    #3.cü evrişim katmanı
    Conv2D(128,(3,3),activation='relu'),
    MaxPooling2D(pool_size=(2,2)),


    #Flatten Düzleştirme
    Flatten(),


    #Tam Bağımlı Katman(Dense)
    Dense(128,activation='relu'),
    Dropout(0.5), #Aşırı Öğrenmeyi önlemek için dropuot ekledik
    Dense(1,activation='sigmoid') #Çıkış katmanı binary classification


])

#Modeli Derleyelim

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#Modelin özeti

model.summary()

#model eğitiyoruz
history=model.fit(X_train,y_train,epochs=10,validation_data=(X_test,y_test),batch_size=32)

model.save("/content/drive/MyDrive/stop_sign_model_v2.h5")

print("Model kaydedildi")

#Modeli Test edelim

#Test etmek için bir resim seç
test_img_path="/content/drive/MyDrive/not_stop/104.jpg"

#Görseli okuyotuz ve model için hazırlıyorum
img=cv2.imread(test_img_path)
img=cv2.resize(img,(64,64))
img=img /255.0
img=np.expand_dims(img,axis=0) #Modelin beklediği şekle getirme

prediction=model.predict(img)

#Sonucu göster
if prediction[0][0]>0.5:
  print("Bu resimde dur işareti var")
else:
  print("Bu resimde dur işareti yok")

from flask import Flask,request,jsonify

app=Flask(__name__)


#Eğittiğim Modeli yüklüyorum

model=tf.keras.models.load_model("/content/drive/MyDrive/stop_sign_model_v2.h5")

#modeli tekrardan compile ediyorum
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

print("model yükleme başarılı")

#Resimlerin işlenip modelin tahmin yapmasını sağlayan fonksiyon

def predict_image(image):
  img=cv2.imdecode(np.fromstring(image.read().np.unit8),cv2.IMREAD_COLOR)
  img=cv2.resize(img,(64,64))
  img=img /255.0
  img=np.expand_dims(img,axis=0) #Modelimin beklediği formata getir
  prediction=model.predict(img)
  return " Stop işareti!" if prediction[0][0]>0.5 else "Stop işareti değil"