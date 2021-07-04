# S.4. Ardışık iki asal sayının toplamı şeklinde yazılan sayılara ardasal sayılar diyelim. Örneğin, 12 sayısı ardasaldır çünkü 5 ve
# 5’ten sonra gelen ilk asal sayı olan 7’nin toplamına eşittir. 16 sayısı ardasal değildir çünkü her ne kadar 16 sayısı iki asal sayının
# toplamı (5+11) olarak yazılsa da 5 ve 11 ardışık asal sayılar değildir. Sizden istenen kullanıcı tarafından girilen bir sayının ardasal
# olup olmadığını ardasal ise ardışık asal sayıları ekrana yazan uygulamayı geliştirmenizdir.
# Not: Sayıların asal olup olmadığını bulmak için derste yazılan asalmi fonksiyonunu kullanabilirsiniz
def asalmi(sayi):
    if sayi > 1:
        for i in range(2, sayi):
            if (sayi % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False
sayi = int(input("bir sayi giriniz :"))
ardasalmi = False
for x in range(2, sayi):
    if asalmi(x):
        for z in range(x + 1, sayi):
            if asalmi(z):
                if x + z == sayi:
                    print("{0} + {1} = {2}".format(x, z, sayi))
                    ardasalmi=True
                break
if not ardasalmi:
    print("sayi ardasal degil")
