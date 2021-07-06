#S.1. a, b, c, d, e birbirinden farklı ab, cd, ba ve dc iki basamaklı ve  sayılar olmak üzere
# ab2 + cd2 = ba2 + dc2 koşulunu sağlayan sayıları ekranda listeleyen uygulamayı geliştiriniz.

for a in range(10):
    for b in range(10):
        if b != a:
            for c in range(10):
                if c != a & c != b:
                    for d in range(10):
                        if d != a & d != b & d != c:
                            ab = (10 * a) + b
                            cd = (10 * c) + d
                            ba = (10 * b) + a
                            dc = (10 * d) + c
                            if (ab * ab) + (cd * cd) == (ba * ba) + (dc * dc):
                                print("ab:{0} cd:{1} ba:{2} dc:{3}".format( ab, cd, ba, dc))
