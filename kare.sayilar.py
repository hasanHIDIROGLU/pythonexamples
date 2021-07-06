#S.3. İki pozitif tamsayının karesinin toplamı olan sayılara kare sayılar diyelim. Girilen iki sayı arasındaki kare sayıları ekrana aşağıdaki gibi yazdıracak uygulamayı geliştiriniz.
# Not: Kullanıcının sırasıyla önce başlangıç, sonra bitiş değerini gireceği varsayılmaktadır. Bunun için bir kontrol yazmanız gerekmemektedir.

baslangic = int(input("Başlangıç değerini giriniz: "))
bitis = int(input("Bitiş değerini giriniz: "))

for x in range(1, bitis + 1):
    for z in range(1, bitis + 1):
        if (x*x) + (z*z) >= baslangic:
            if (x*x) + (z*z) <= bitis:
                print("{0}^2 + {1}^2 = {2}".format(x, z, (x*x) + (z*z)))
