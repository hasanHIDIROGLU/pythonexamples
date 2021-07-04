# S.1. Altı rakamlı bir sayıdan tersini çıkarınca elde edilen sayı, ilk iki rakamının oluşturduğu sayı ile son iki rakamının oluşturduğu
# sayının çarpımına eşittir. Bu sayıyı bulan uygulamayı geliştiriniz.
# Rakamların sayı oluşturmaları ile ilgili örnek: Sayı 987654; ise tersi 456789, ilk iki rakamın oluşturduğu sayı 98, son iki rakamın
# oluşturduğu sayı 54’tür.
sayi = 100000
while len(str(sayi)) == 6:
    metinsayi = str(sayi)
    tersi = metinsayi[::-1]
    ilkiki = metinsayi[0:2]
    soniki = metinsayi[-2:]
    if (sayi - int(tersi)) == int(ilkiki) * int(soniki):
        print(sayi)
    sayi += 1
