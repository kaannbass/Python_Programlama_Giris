#Sayılar ve Stringlere giris 
9
9.2
print("Hello AI Era")

type(9)

type(9.2)

# Stinglere yakindan bakalim 

"a" + "b"  #ab

"a" "b"    #ab

"a" " b"   #a b

"a"*3      #aaa

# Bolme cikarma olmuyor str çünkü

#String Metodları - LEN

gel_yaz = "gelecegi_yazanlar"
#del a
a = 9 
b = 10

a*b

len(gel_yaz)

len("gelecegi_yazanlar")
#len kac tane terim olduğunu g�sterir

#Upper(Buyuk harf hepsi) - Lower -islower(kucuk harf)
gel_yaz.lower()

gel_yaz.islower()
B = gel_yaz.upper()

B.islower()
B.isupper()

#Karakter Degistirme Replace kaşıcı degisiklik yapmaz 

gel_yaz.replace("e","a") #e leri a yaptı
gel_yaz.replace("a", "i") # a ları i yaptı metindeki bütün -a ları 

# istenmeyen karekterleri kırpmak için kullanılı strip()

gel_yaz = " gelecegi_yazanlar "
gel_yaz.strip() #bos�luklari sildi

gel_yaz = "*gelecegi_yazanlar*"
gel_yaz.strip("*") # *'ları sildi

dir(gel_yaz)

gel_yaz = "gelecegi_yazanlar"

gel_yaz.capitalize() # ilk harfi büyütür

gel_yaz.title() # Her bir kelime buyuk harf baslar

#Karakter Dizilerinde Altkume is�lemi - substrings
#[] = bir seçim işlemi 

gel_yaz[0] # g olarak gelir ekrana

gel_yaz[1] # e olarak gelir ekrana

gel_yaz[0:3] #gel olarak çıktı 0 dan 3 e kadar olan terimi getirir

#Degiskenler

a = 9
b = "ali_uzaya_git"

type(100)
type(100.2)
type(1+2j)

c = 100.2

#TYPE_Donusumleri

toplama_bir = input()
toplama_iki = input()

type(toplama_bir)

int(toplama_bir) + int(toplama_iki)

11.0
int(11.0)
float(12)
type(str(12))


print("Selam")

print("gelecegi","yazanlar",sep = "_") 

#Veri Yapilari

#Listeler
#2 yol vardir.
#[]
#list()

notlar = [90,80,70,50]

type(notlar)

liste = ("a",19.3,90)
liste_genis = ("a",19.3,90,notlar)

len(liste)

type(liste[0])
type(liste[2])
type(liste[3])

tum_liste = [liste,liste_genis]

#del tum_liste

liste = [10,20,30,40,50]
liste[:2]

yeni_liste = ["a",10,[10,20,30,40,50]]


yeni_liste[2]

yeni_liste[2][3]

#Liste ekleme silme degistirme

liste2 = ["ali","veli","berkcan","ayşe"]

liste2[1] = "velinin_babası"

liste2[:3] = "alinin_babasi","velinin babası","berkcanın_babası"

liste2

liste2 = ["ali","veli","berkcan","ayşe"]

liste2 = liste2 + ["kemal"]

#del liste2[2]

dir(liste2)


# append (kal�c� �ekilde ekler) remove (siler)

liste = ["ali","veli","berkcan","ays�e"]


liste.append("isik")

liste.remove("berkcan")

liste

#indekse g�re eleman ekleme insert

liste =["ali","veli","isik"]

#2. sayfada ama ekledim burayada 

#indekse g�re eleman ekleme insert - pop eleman silme 

liste =["ali","veli","isik"]

liste.insert(0,"ayse") #['ayse', 'ali', 'veli', 'isik']

liste[0]

liste.insert(2,"mehmet")

liste

liste.insert(5,"kaan")

len(liste)

liste.insert(len(liste),"beren")#listenin sonuna beren yazd� 
liste

liste.pop(0) # ayse sildi

liste
# count eleman frekanslar�n� ver�yor

liste.count("ali") 
liste.count("mehmet")

liste_yedek = liste.copy()

#extend iki listeyi birle�tiriyor daha oncede gordum ama bu daha k�sa
#de�i�tirerek birle�tirme yap�yor kal�c� �ekilde

liste.extend(["a","b",10])
liste

#index ka��nc� indexde oldugunu gosterir
liste.index("ali")
#reverse() elemanlar� terse �evirir
liste.reverse()
liste


#sort s�ralama yapar

liste2 = [10,20,80,20,30,50]

liste2.sort()

liste2
liste2.count(20)

#listeyi komple siler
liste2.clear()


#Veri Yap�lar� tuple
#tuple liste ile ayn� fark� tuple degi�tirilemez!!! 
#2. bir olay� index i�lemleri ve s�ral� olmas�d�r.
t = ("ali","veli",1,2,3,2,[1,2,3,4])

##tuple()
# tek elemanl� tuplelarda str anlayab�l�r sonuna bir "," koydugunda tuple oluyor

t = ("eleman",)

t = ("ali","veli",1,2,3,[1,2,3,4])

t[1]

#t[2] = 99
#t[0] + "ali"
#t[0] = t[0] + "ali"

#S�zl�k yap�lar� Dictionary 

# Sozluk olu�turma 
sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}

len(sozluk)

sozluk["REG"]

#Eleman ekleme ve c�karma

sozluk ["GBM"] = "Gradient Boosting Mac"

sozluk
sozluk["REG"] = " coklu Dogrusal Regresyok "

sozluk

sozluk[1] = "Yapay Sinir Aglar�"
sozluk

l = [1]

sozluk[l] = "yeni bir sey"

t = ("tuple",)
sozluk[t] = "yeni bir sey"

sozluk


#Setler
#�zellikleri :
#sirasizdir,de�erleri essizdir,de�istirilebilirdir,Farkl� tipleri bar�nd�rab�rabilir

#Set olu�turma

s = set()
l = (1,"a","ali",123)

s = set(t)

ali = "lutfen_ata_bakma_uazaya_git"

s = set(ali)
s
l = ["ali","lutfen","uzaya","bakma","git","ali","git"] 

s = set(l)

s


len(s)

l[0]
s[0]

# Eleman ekleme & cikarma

l = ["gelecegi","yazanlar"]

s = set(l)

dir(s)

s.add("ile")
s

s.add("gelecege_git")

s


s.add("ile")
s

s.remove("ali")

s
#hata bulup kod ak�s�n� kesmes�n d�ye discard kullan�l�yor

s.discard("ali")

#Setler - Klasik Kume Islemleri
#
# =============================================================================
# difference() ile iki kumenin fark�n� ya da "-" ifadesi ile ayn� sonucu verir
# intersection () iki kume kesimi ya da & ifadesi 
# union () iki kumen�n birlesimi
# symmetric_difference() ikisinde de olmayan 
# 
# =============================================================================


set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2) # 5 gelir
set1 - set2 # 5 gelir

set2.difference(set1) # 2 gelir
set2 - set1 # 2 gelir

set1.symmetric_difference(set2) # 2 ve 5 degerler�n� verd� 
set2.symmetric_difference(set1) # 2 ve 5 degerler�n� verd� 

#Kesi�im ve Birle�imler

# intersection () iki kume kesimi ya da & ifadesi 

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2) # 1 ve 3 

set1 & set2 # 1 ve 3 

kesisim = set1 & set2
kesisim

birlesim = set1.union(set2) #1,2,3,5 birlesim

birlesim

set1.intersection_update(set2) # yeni set1 1 ve 3 olarak de�i�tirdi
set1

#Setlerde sorgu islemleri 

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

# iki kumenin kesisiminin bos olup 
# olmadiginin sorgulanmas� ?

set1.isdisjoint(set2) # iki kumenin kesisimi bos de�il 

#bir kumenin butun elemanlarinin baska bir kume 
#i�erisinde yer alip almadigi

set1.issubset(set2) # set1 set 2 nin alt kumesimidir diye sorguladi

#  k�meler kapsay�p-kapsamama sorgusu

set2.issuperset(set1) 













