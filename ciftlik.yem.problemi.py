# S.3. Bir çiftlikte bulunan koyunların beslenmesi şu şekilde yapılmaktadır. Öncelikle besleme makinesine belirlenen bir miktarda
# yem doldurulmaktadır. Daha sonra görevli personel koyunlara verilecek günlük üst limit yem miktarını uygulamaya girmektedir.
# Uygulama 1,3,5 gibi tek günlerde üst limitin yarısı, çift günlerde ise üst limitin dörtte biri kadar yem vermektedir. Sizden istenen
# belirlenen yem miktarına ve üst limit değerlerine göre günlük yem miktarlarını ve yemin kaç gün yeteceğini hesaplayan
# uygulama geliştirmenizdir. Aşağıda uygulamaya ilişkin örnek çıktılar verilmiştir. Not: Son gün kalan miktar üst limitin
# yarısından veya dörtte birinden az ise bu durumda kalan yemin tamamı verilmelidir.
import math
baslangic = int(input("başlangıç değerini giriniz:"))
bitis = int(input("bitiş değerini giriniz:"))
for x in range(baslangic, bitis + 1):
    for z in range(1, x ):
        for y in range(z + 1, x ):
            if math.hypot(z, y) == x:
                print(z, y, x)
                print(y, z, x)
