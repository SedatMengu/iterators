# iterator : adımlama işini yapan nesnedir. bütün elemanları teker teker  geziyor ve nerede kaldığınıda unutmuyor.
# iterable : üzerinde adımlama yapılabiln demektir. döngülerle kullanabileceğimiz büün nesneler iterable dır.
# iteration : adımlama demektir. bir nesnenin elemanlarını teker teker adımlama işlemşne denir.
# __iter__() , __next__() dunder metotları:


# Python'da bir iterator, bir veri yapısının elemanlarını sırayla döndüren bir nesnedir.
# Iteratorlar, bellekte tüm veriyi tutmak yerine, elemanları sırayla üretirler, bu nedenle bellek kullanımı açısından oldukça verimlidirler.
# Iteratorler, "iter()" ve "next()" metodlarını uygulayan bir nesne olmalıdır. 
# "iter()" metodu, nesneyi bir iteratora dönüştürür ve "next()" metodu, bir sonraki elemanı döndürür.
# Birçok veri yapısı Python'da iterator olarak kullanılabilir, örneğin listeler, demetler, sözlükler ve dosyalar. 
# Özellikle büyük veri kümeleri için iterator kullanmak, veri bellekte tutulmadığı için performans açısından büyük avantajlar sağlar.


# tipini bilmediğimiz bir şeyin iterable olup olmadığını nasıl anlarız ?
# sayilar=[1,2,3]
#print(dir(sayilar)) dediğimizde çıkan dunder metotlar arasında __iter__() objesi var ise sayilar objesi iterable dır denir ve döngüler ile kullanılabilir. 

# iterable demek adım atılabilen demek.

i_sayilar=[1,2,3,4,5].__iter__()        # bu şekilde sayilar dizisi iterable bir dizi oldu. iterable olması listenin tamamını kullanmıyorum , adım adım takip ederek ihtiyacımı karşılıyorum demektir.
# i_sayilar=iter([1,2,3,4,5])             # yukarıdaki ile aynı sonucu verdi. bu daha şık oldu. listeyi adımlara böldük ve next metodu ile adım adım alacağızç

# print(i_sayilar.__next__())          # bu ifade her zaman 0.indexi yazdırır.
# # print(next(i_sayilar))             # yukarıdaki ile aynı sonucu verir.
# print(i_sayilar.__next__())          # bu ifade eklendiğinde 1.index i yazdırır.
# # print(next(i_sayilar))             # yukarıdaki ile aynı sonucu verir.
# print(i_sayilar.__next__())          # bu ifade eklendiğinde 2.index i yazdırır.
# # print(next(i_sayilar))             # yukarıdaki ile aynı sonucu verir.
# print(i_sayilar.__next__())          # bu ifade eklendiğinde 3.index i yazdırır.
# # print(next(i_sayilar))             # yukarıdaki ile aynı sonucu verir.
# print(i_sayilar.__next__())          # bu ifade eklendiğinde 4.index i yazdırır.
# # print(next(i_sayilar))             # yukarıdaki ile aynı sonucu verir.
# print(i_sayilar.__next__())          # bu ifade eklendiğinde 5.index i yazdırır. 5.index olmadığı için "StopIteration" hatası verdi.
# # print(next(i_sayilar))             # yukarıdaki ile aynı sonucu verir.


while True:
    try:
        sayi=next(i_sayilar)
        print(sayi)
    except StopIteration:
        break



