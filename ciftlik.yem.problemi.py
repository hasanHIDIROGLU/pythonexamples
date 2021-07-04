# S.3. Bir çiftlikte bulunan koyunların beslenmesi şu şekilde yapılmaktadır. Öncelikle besleme makinesine belirlenen bir miktarda
# yem doldurulmaktadır. Daha sonra görevli personel koyunlara verilecek günlük üst limit yem miktarını uygulamaya girmektedir.
# Uygulama 1,3,5 gibi tek günlerde üst limitin yarısı, çift günlerde ise üst limitin dörtte biri kadar yem vermektedir. Sizden istenen
# belirlenen yem miktarına ve üst limit değerlerine göre günlük yem miktarlarını ve yemin kaç gün yeteceğini hesaplayan
# uygulama geliştirmenizdir. Aşağıda uygulamaya ilişkin örnek çıktılar verilmiştir. Not: Son gün kalan miktar üst limitin
# yarısından veya dörtte birinden az ise bu durumda kalan yemin tamamı verilmelidir.

yem_miktari = int(input("yem miktarını giriniz:"))
ust_limit = int(input("üst limit miktarını giriniz:"))
tek_gun_yem_miktari = ust_limit // 2
cift_gun_yem_miktari = ust_limit // 4
gun_sayisi = 1
while yem_miktari > 0:
    if yem_miktari > tek_gun_yem_miktari:
        print("{0}. gün verilen yem : {1}".format(gun_sayisi,tek_gun_yem_miktari))
        gun_sayisi += 1
        yem_miktari -= tek_gun_yem_miktari
        tek_gun_yem_miktari,cift_gun_yem_miktari=cift_gun_yem_miktari,tek_gun_yem_miktari
    else:
        print("{0}. gün verilen miktar : {1}".format(gun_sayisi,yem_miktari))
        yem_miktari=0
