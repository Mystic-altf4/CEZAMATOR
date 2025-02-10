import random
katsayı= input("Lütfen ceza acısını belirleyin(1,5) ")
isim = input("Lütfen isminizi giriniz: ")
i = random.randint(1,3)
if katsayı == "1":
    if i == 1:
        print(f" İsim: {isim} Ceza: 2 dakikalığına tek ayak üstünde durma cezası.")
    elif i == 2:
        print(f" İsim: {isim} Ceza: Sözlü Uyarı.")
    elif i == 3:
        print(f" İsim: {isim} Ceza: Sınıftan Atılma.")
   
elif katsayı == "2":
    if i == 1:
        print(f" İsim: {isim} Ceza: Acı Sos içmek.")
    elif i == 2:
        print(f" İsim: {isim} Ceza: Sözlü Uyarı Tutanağı.")
    elif i == 3:
        print(f" İsim: {isim} Ceza: Ek ödev (3 KİTAP).")
    
elif katsayı == "3":
    if i == 1:
        print(f" İsim: {isim} Ceza: Ek sınav (120 soru).")
    elif i == 2:
        print(f" İsim: {isim} Ceza: Yazılı Uyarı Tutanağı.")
    elif i == 3:
        print(f" İsim: {isim} Ceza: Habanero Sosu içmek.")
    

elif katsayı == "4":
    if i == 1:
        print(f" İsim: {isim} Ceza: Okuldan Atılma.")
    elif i == 2:
        print(f" İsim: {isim} Ceza: Disiplin.")
    elif i == 3:
        print(f" İsim: {isim} Ceza: Akrep Sosu (korkmayın acı sos) içmek.")

elif katsayı == "5":
    if i == 1:
        print(f" İsim: {isim} Ceza: HAYALET BİBER (TEKLENECEK).")
    elif i == 2:
        print(f" İsim: {isim} Ceza: ClubStep tekle.")
    elif i == 3:
        print(f" İsim: {isim} Ceza: Müebbet Hapis.")

elif katsayı == "6":
    if i == 1:
        print(f" İsim: {isim} Ceza: Sınıf ortasında twerk atmak.")
    elif i == 2:
        print(f" İsim: {isim} Ceza: Cuphead'i EXPERT modda tekle.")    
    elif i == 3:
        print(f" İsim: {isim} Ceza: Bir ay boyunca reddit'te mahsur kalmak (çıldırırsın).")
else:
    print("ERROR CANCELLED PROGRAM")