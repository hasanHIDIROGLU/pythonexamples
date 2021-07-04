# S.2. Kullanıcı tarafından girilen iki değer arasındaki her bir değer hipotenüs uzunluğu olacak şekilde kenarları tamsayıdan oluşan
# bir dik üçgen çizilebiliyorsa bu dik üçgenlerin kenar uzunluklarını ekrana yazan uygulamayı geliştiriniz. Not: Kullanıcının
# sırasıyla önce başlangıç, sonra bitiş değerini gireceği varsayılmaktadır. Bunun için bir kontrol yazmanız gerekmemektedir.
import math
baslangic = int(input("başlangıç değerini giriniz:"))
bitis = int(input("bitiş değerini giriniz:"))
for x in range(baslangic, bitis + 1):
    for z in range(1, x ):
        for y in range(z + 1, x ):
            if math.hypot(z, y) == x:
                print(z, y, x)
                print(y, z, x)
