# -*- coding: utf-8 -*-
"""PandasGenelTekrar.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jgyDL2_0QmiDcpm51_XMN_jJhHxdNUPA
"""

import pandas as pd



obje=pd.Series([1,"Halil",3.5,"Eren"])
obje
#objeyi bana series şeklinde yazdırıyor.
obje[2]
#istediğim indexteki objeyi bana veriyor
obje=pd.Series([1,"Halil",3.5,"Eren"],index=["a","b","c","d"])
obje
#objenin indexini değiştirmiş olduk

puan={"Ali":90,"Halil":80,"Eren":70}
puan=pd.Series(puan)
puan
#sözlük yapısını seriese çevirmiş olduk
puan[puan>85]
#puanı 85ten büyük olan değerleri yazdırdık
puan["Ali"]=60
puan
#ali'nin puanını değiştirmiş olduk
"Halil" in puan
#olup olmadığını yazdırmış olduk

#eksik veri olup olmadığını bulmak için isnull metodu kullanılır
puan.isnull()

#iki değişkenin karşılılı değerleri tablo olarak görmek istersek crosstab metodu kullanılır

#veriyi nasıl grafikleştireceğimizi görmek için öncelikle %matplotlib inline diyoruz
#sonra seriesadı.sutuismi.plot(kind="grafiktürü")

"""DataFrame"""

#series tek bir sutundan oluşur dataframe is birden fazla sutundan oluşur

veri={"isim":["Ali","Can","Ayşe","Buse","Alp","Nur"],
      "puan":[90,80,85,75,95,60],
      "cinsiyet":["E","E","K","K","E","K"],
      "spor":["Futbol","Kayak","Yüzme","Tenis","Karate","Sörf"]}
veri=pd.DataFrame(veri)
veri

veri.head()
#ilk 5 veriyi gösterir

veri.tail(2)
#son 2 veriyi gösterir

#sutunların sırasını değiştirebiliriz
veri=pd.DataFrame(veri,columns=["isim","spor","puan","cinsiyet"])
veri

#indexlere etiket atayabiliriz
df=pd.DataFrame(veri,index=["bir","iki","uc","dort","bes","altı"])
df

veri["spor"]
#tek bir sutun alabiliriz

veri.spor
#bu şekilde de alabiliriz o sutunu

df.loc[["bir"]]
#istediğimiz satırı bu şekilde alabiliyoruz

#dataframe değer eklemek istiyorsam bu şekilde ekleyebilirm
deger=[17,18,19,20,14,16]
df["yas"]=deger
df

#dataframe içine sutun eklemek istiyorsam üstüne koşulda eklemek istiyoırsam şu şekilde yaparım
veri["geçti"]=veri.puan>75
veri
#bana boolean döndürüyor

#sözlük içinde sözlük oluşturduk
#Dataframe yapısı dışraki sözlüğü sutun olarak içteki sözlüğü satır olarak alır
notlar={"Mat":{"Efe":90,"Halil":70,"Nur":85},
        "Fizik":{"Efe":75,"Halil":70,"Nur":42}}
notlar=pd.DataFrame(notlar)
notlar
notlar.index.name="İsim"
notlar.columns.name="Ders"
notlar

#df veri yapısını 2 boyutlu diziye dönüştürüyoruz burada
notlar.values

#index değiştirilemez hale getirdiğimiz format bu şekilde
index=veri.index

"""# **  İNDEXLEME-SEÇME-FİLTRELEME**:\"""

import numpy as np

nesne=pd.Series(np.arange(5),index=["a","b","c","d","e"])
nesne

nesne[[0,2]]

#2den küçük değerleri bastırdık
nesne[nesne<2]

#indexleri dilimleme pythondan farklıdır son nokta dilimlemeye dahildir
nesne["a":"c"]

#dilimlenen kısma yeniden değer atabiliriz
nesne["a":"c"]=5
nesne

veri=pd.DataFrame(np.arange(16).reshape((4,4)),
                  index=["Bursa","Ankara","İstanbul","İzmir"],
                  columns=["bir","iki","üç","dört"])
veri

veri[["bir","iki"]]

veri[:3]

veri[veri["dört"]>5]

#veri içerisinde 5'ten küçük verilere 0 değeri yazdırıldı
veri[veri<5]=0
veri

#1.ci indexe sahip satırın değerleri karşımızı gelir
veri.iloc[1]

#1.ci indexe sahip satırın belrili sutunlarını seçmek istersek
veri.iloc[1,[1,2,3]]

#birden çok satırın birden çok sutunlarını yazdırabiliriz
veri.iloc[[1,3],[1,2,3]]

#loc için etiket sutunları kullanılır
veri.loc["Ankara",["iki","üç"]]
#seçeceğimiz sutun ve satır isimlerini yazıyoruz

veri=pd.Series(np.arange(5),index=["a","b","c","d","e"])
veri

"""# **  önemli metodlar**"""

s=pd.Series([1,2,3,4],index=["a","b","c","d"])
s

#reindex metodu sayesinde indexlerin sırasını değiştirebiliyorum
s2=s.reindex(["b","d","a","c","e"])
s2

s3=pd.Series(["mavi","sarı","mor"],index=[0,2,4])
s3

#ffill fonksiyonu, eksik değerleri ortalamayla, medyanla, en son değerle veya belirli bir değerle doldurma gibi farklı stratejiler sunar.27 Haz 2023
s3.reindex(range(6),method="ffill")

df=pd.DataFrame(np.arange(9).reshape((3,3)),index=["a","c","d"],columns=["bir","iki","üç"])
df

df2=df.reindex(["d","c","b","a"])
df2

#oluşturduğum df'in sutun isimlerini revize ettim
isim=["efe","halil","nur"]
df.reindex(columns=isim)

df.loc[["c","d","a"]]

veri=pd.DataFrame(np.arange(16).reshape((4,4)),
                  index=["Bursa","Ankara","İstanbul","İzmir"],
                  columns=list("ABCD"))
veri

veri.drop(["Bursa","Ankara"])

#sutun sileceksem axis=1
veri.drop("A",axis=1)

#satır sileceksem axis=0
veri.drop("Bursa",axis=0)

veri.mean(axis=0)

#her bir satır için sutunların ortalamasını yazdırabiliriz
veri.mean(axis=1)

"""## Aritmetik İşlemler"""

import pandas as pd; import numpy as np

s1=pd.Series(np.arange(4),index=["a","c","d","e"])
s2=pd.Series(np.arange(5),index=["a","c","e","f","g"])
s1
s2

#2 tane arreyi topladık ortakları kesiştirdik ortak olmayanları null olarak default atadık
s1+s2

df1=pd.DataFrame(np.arange(6).reshape((2,3)),columns=list("ABC"),index=["Ankara","İstanbul"])
df2=pd.DataFrame(np.arange(9).reshape((3,3)),columns=list("ACD"),index=["Ankara","İstanbul","İzmir"])

df1

df2

df1+df2

#eşleşmeyen  yerlere 0 değerini atadık
df1.add(df2,fill_value=0)

#1/df dersek çarpmaya göre tersini almış oluruz
1/df1

df2.sub(s2,axis="index")

"""## SIRALAMA"""

s=pd.Series(range(5),index=["e","d","a","b","c"])
s

#indexlerine göre sıralıyoruz
s.sort_index()

df=pd.DataFrame(np.arange(12).reshape((3,4)),index=["two","one","three"],columns=["d","a","b","c"])
df.sort_index()

s2=pd.Series([5,3,-1,9])
s2

#değerler artan sıraya göre sıralanmaya başlıyor
s2.sort_values ()

df2=pd.DataFrame({"a":[5,3,-1,9],"b":[1,-2,0,5]})
df2

#spesifik olarak b sutununu sırala diyoruz
df2.sort_values(by="b")

veri=pd.read_csv("student_performance.csv")
veri

veri.head()

#küçükten büyüğe doğru bir sıralama var burada
veri.sort_values(by="AttendanceRate")

veri.sort_values(by=["Name","Gender"])

"""## Verileri **özetleme**"""

#eksik veri bulunan satırların ortalamasını hesaplamamak için
df.mean(axis=1,skipna=False)

#satır ve sutunlardaki max değri bulmak için
#min için ise idxmin yazıcaz
df.idxmax()

#veri setimizin özet bilgileri karşımıza geliryor bu şekilde
veri.describe()

#pandasta korelasyon 2 değişken arasındaki ilişkiyi inceler pandasta korelasyon katsayısının nasıl bulunacağı için
#korelasyon katsyısı -1 ile 1 arası bir değer alıyor
iris.corr()
#yazarsak butun değişkenlerin birbiri arası kolerasyon katsayıları kıyaslanır

iris.corrwith(iris.Canak_yaprak_boyu)
#çanak yaprak boyu ile diğer değişkenlerin 2'li kolerasyon kat sayıları karşımıza geldi

s=pd.Series(["b","b","b","b","c","c","a","a","a"])
s

s.unique()

s.value_counts()

#veri okumak için eğer dosya , ile ayrılmışsa read_csv eğer  bir tab boşlukla ayrılmışsa read_table metodu kullanılır

#eksik veri seti ile karşılaşırsak dış kaynaktan aldığımız verilerde
#eksik veriler nan ile gösteriliyor
ekaik_veri={"sutun ismi":[eksik veri],"sutun ismi":[eksik veri]}
df=pd.read_table("dosya adı.türü",sep="neye göreayıracağımız , veya - vs",na_values=["eksik veri"])
df

#mesela veri setini pcde bir yere kaydetmek istiyorsam
df=pd.read_table("dosya adı")
df
df.to_csv("dosya adı")
#jupytere kaydetmek istioyrsam bu şekilde
df.to_csv("uzantı ")
#pcde bir yere kaydetmek istiyorsam

"""EKSİK VERİ

"""

#pandas ile eksik verilerle nasıl oynayacağımzıı göreceğiz
import pandas as pd ; import numpy as np

s=pd.Series(["Halil",np.nan,"Eren","Nur"])
s
s.isnull()

s[3]=None
s
#belirlediğim indexi none'a çevirdim

s[s.notna()]
s

from numpy import nan as NA
#eksik verilerle oynamak için bu kütüphaneyi import eklememiz lazım

df=pd.DataFrame([[1,2,3],[4,NA,6],[NA,NA,NA],[NA,5,6]])
df

df.dropna()

df.dropna(how="all")
#bütün değerleri eksik olan satırı kaldırdı

df[1]=NA
df
df.dropna(axis=1,how="all")
#bütün değerleri eksik olan sutunu kaldırdı

df.dropna(thresh=1)
#en az 1 değeri olan satırlar ya da satır yazdırılır

#eksik veri yerine başka bir değer atamak istersek fillna metodu kullanılır
df
df.fillna(0)

#sözlük verisi kullanılarak her bir sutun içersindeki eksik değerlere farklı bir değer atayabilriz
df.fillna({0:15,1:25,2:35})
#ilki hangi sutun ikincisi ne atıyacağımız demek

#fillna metodundan sonra modifiye etmek istersek
df.fillna(0,inplace=True)
df

df=pd.DataFrame([[1,2,3],[4,NA,6],[NA,NA,NA],[NA,5,6]])
df

#eksik veriler yerine bir üst satırdaki verileri atamak için
df.fillna(method="ffill")

df.fillna(method="ffill",limit=1)
#burada limit demek kısıtlıyoruz sadece 1 tane sutun üstekinin değerini alıyor altında eksik veri varsa o aynen kalıyor

#eksik veri yerine o stunun ortalamasını yazmak istiyorsam eğer napıcam
veri=pd.Series([1,0,3.5,NA])
veri

veri.fillna(veri.mean())

df

df.fillna(df.mean())

"""Veri Dönüştürme

"""

import pandas as pd

#tekrar eden satırlar bulunabilir
veri=pd.DataFrame({"a":["bir","iki"]*3,"b":[1,1,2,3,3,4]})
veri

#dublicated metodu tekrar edip etmediğni gösterir
veri.duplicated()

veri.drop_duplicates()
#tekrar eden satırları siler

#yeni bir sutun ekleyip 0-6 arası değer ataması yaptırdım
veri["c"]=range(6)
veri

#sadece bir sutundaki değerlerin tekrar edenlerini silmek istersem eğer
#veri.dublicate(["a"])

#sondan başlayarak tekrar eden değerleri bulmak istiyorsak
veri.duplicated(["a","b"],keep="last")

vs=pd.DataFrame({"isim":["Ali","Can","Nur","Efe","Ata"],
                "puan":[60,50,70,80,40]},index=["Öğrenci  1","Öğrenci  2","Öğrenci  3","Öğrenci  4","Öğrenci  5"])
vs

sınıf={"Ali":"A","Can":"A","Nur":"B","Efe":"B","Ata":"B"}

#SINIFI EKLEMEK İÇİN
ad=vs["isim"].str.capitalize()

vs["sube"]=ad.map(sınıf)
vs

nt=pd.Series([80,70,90,60])
nt

import numpy as np

#önce değiştireceğimiz veri sonra ise onu neyle değiştireceksek onu yazıyoruz
nt.replace(70,np.nan)
nt.replace([70,60],[np.nan,0])

nt.replace({80:100,60:0})

df=pd.DataFrame(np.arange(12).reshape((3,4)),index=["bir","iki","üç"],columns=["ali","efe","eda","can"])
df

#büyük harfe geçtim.title diyerek indexlerin ilk harfini upper diyerek sutunların hepsini büyük yazdırdım
df.rename(index=str.title,columns=str.upper)

#sözlük şeklinde değişiklikler yaptık aynı anda hep index hem sutun simi değiştirdik
df.rename(index={"bir":"on"},columns={"ali":"halil"})

HİYERAKLİŞ İNDEXLER
ÇOKLU İNDEX OLARAKTA BİLİNİR

import numpy as np ; import pandas as pd

veri=pd.Series(np.random.randn(8),index=[["a","a","a","b","b","b","c","c"],[1,2,3,1,2,3,1,2]])
veri

veri.index

veri["a"]

veri["b":"c"]
#pythondan farkı en sonuncusunuda dilimi ekliyor yani c'yi

veri.loc[["b","c"]]

#içindeki 1.ci indexleri almak istersem
veri.loc[:,1]

#tablo halinde göstermek istiyorsam bu şekilde gösteririm
veri.unstack()

#tekrardan eski haline döndürmek istiyorsam
veri.unstack().stack()

vs=pd.DataFrame(np.arange(12).reshape((4,3)),index=[["a","a","b","b"],[1,2,1,2]],columns=[["say","say","soz"],["mat","fiz","edb"]])
vs

vs.index.names=["sınıf","sinav"]
vs.columns.names=["alan","ders"]
vs

vs["say"]

vs.swaplevel("sınıf","sinav")

vs.sort_index(level=1)
#1.ci seviyeye göre sıralanmış oldu

veri=pd.DataFrame({"x":range(8),"y":range(8,0,-1),
                  "a":["bir","bir","bir","bir","iki","iki","iki","iki"],
                   "b":[0,1,2,3,0,1,2,3]})
veri

#bu veri setinin a ve b sutunlarını satır indexi şeklinde yazalım
veri2=veri.set_index(["a","b"])
veri2

#set index metodunda satıra taşınan indexler sutundan kaldırırlı eğer istersek dropfall metodu ile aynı kalır
veri3=veri.set_index(["a","b"],drop=False)
veri3

#herşeyi eski haline getirme metodu buda.
veri2.reset_index()

"""VERİ BİRLEŞTİRME
BAZEN VERİ SETLERİ FARKLI KÜTÜPHANELERDEN GELEBİLİR BİZDE SATIRLARI BİRLEŞTİREBİLİRİZ

"""

import pandas as pd ; import numpy as np

v1=pd.DataFrame({"anahtar":["a","b","c","c","d","e"],"say1":range(6)})
v2=pd.DataFrame({"anahtar":["b","c","d","e"],"say2":range(4)})

v1

v2

#anahtar sutununa göre veri setleri otomatik birleştirilmiş oldu
pd.merge(v1,v2)

pd.merge(v1,v2,on="anahtar")

#birleştirilecek sutun isimleri farklı ise bu sutunları ayrı ayrı belirtebiliriz
v3=pd.DataFrame({"anahtar1":["a","b","c","c","d","e"],"say1":range(6)})
v4=pd.DataFrame({"anahtar2":["b","c","d","e"],"say2":range(4)})
pd.merge(v3,v4,left_on="anahtar1",right_on="anahtar2")
#v3teki a değeri ekrana yazılmadı eğer a'yıda ekrana yazdırmak istiyorsam
#how="outer" metodunu kullanıyouz
#how="left" yazarsak soldaki veriye göre veri tablosu oluştur diyoruz
#how="inner" iki verinin kesişimine göre birleştiriyor
pd.merge(v3,v4,left_on="anahtar1",right_on="anahtar2",how="outer")

v1=pd.DataFrame({"anahtar":["a","b","c","c","d","e"],"say1":range(6),
                 "rakam":["bir","üc","iki","bir","bir","iki"]})
v2=pd.DataFrame({"anahtar":["b","c","d","f"],"say2":range(4),
                 "rakam":["bir","bir","iki","iki"]})

v1

v2

#bu iki veri setini anahtar ve rakam sutununa göre birleştirelim
pd.merge(v1,v2,on=["anahtar","rakam"])

#mesela burada v1 ve v2 ikisinde de anahtar ve rakam sutunları var ama ben anahtar sutuna göre birleştirme yap dediğim için rakam sutunlarını python kendi otomatik olarak x ve y olarak adlandırdı

pd.merge(v1,v2,on=["anahtar"],how="outer")

#ben bu python pandasın kendi otomatik adlandırılmasını değiştirebilirim rakam_x  ve rakam_y adlandırılmalarını kendi belirttiğim şekilde adlandırabilirim
pd.merge(v1,v2,on="anahtar",how="outer",suffixes=("_veri1","_veri2"))

df1=pd.DataFrame({"harf":["a","a","b","b","a","c"],"say":range(6)})
df2=pd.DataFrame({"deger":[3,5,7]},index=["a","b","c"])

df1

df2

#df2 veri setinin indexlerine göre veri setini birleştirmek istersem eğer
pd.merge(df1,df2,left_on="harf",right_index=True)

sag=pd.DataFrame([[1,2],[3,4],[5,6]],index=["a","c","e"],columns=["halil","ibrahim"])
sol=pd.DataFrame([[7,8],[9,10],[11,12],[13,14]],index=["b","c","d","f"],columns=["efe","ata"])
#

sol

sag

pd.merge(sag,sol,right_index=True,left_index=True,how="outer")

sol.join(sag,how="outer")

diger=pd.DataFrame([[1,3],[5,7],[9,11]],index=["a","b","f"],columns=["buse","sena"])
diger

sol.join([diger,sag])

dizi=np.arange(20).reshape(4,5)
dizi

#dizi ismindeki diziyi kendisiyle birleştirmiş oluyorum bu şekilde
#sutun olarak birleştiridğim için axis=1
np.concatenate([dizi,dizi],axis=1)

veri1=pd.Series([0,1],index=["a","b"])
veri2=pd.Series([2,3,4],index=["c","d","e"])

veri3=pd.Series([5,6],index=["f","g"])

#concat metodu verileri satır olarak birleştirir sutun olarak birleştirmek istersek axis=1
pd.concat([veri1,veri2,veri3],axis=1)

veri4=pd.Series([10,11,2],index={"a","b","c"})
pd.concat([veri1,veri4],axis=1,join="inner")