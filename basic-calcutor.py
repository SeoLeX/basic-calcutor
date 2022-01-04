print("Lütfen istediğiniz işlemi seçiniz -\n" \
        "1. Toplama\n" \
        "2. Çıkarma\n" \
        "3. Çarpma\n" \
        "4. Bölme\n")
  
  

select = int(input("İstediğiniz işleminin sayı değerini giriniz: 1, 2, 3, 4 :"))
  
number_1 = int(input("1. sayıyı giriniz: "))
number_2 = int(input("2. sayıyı giriniz: "))
  
if select == 1:
    print(number_1, "+", number_2, "=", number_1 + number_2)
  
elif select == 2:
    print(number_1, "-", number_2, "=", number_1 - number_2)
elif select == 3:
    print(number_1, "*", number_2, "=", number_1 * number_2)
  
elif select == 4:
    print(number_1, "/", number_2, "=", number_1 / number_2)
else:
    print("Geçersiz değer")