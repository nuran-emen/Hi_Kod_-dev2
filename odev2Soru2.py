kullaniciAdi = input("Kullanıcı adı girin:")
parola = input("Lütfen 6 karakterden oluşan bir parola belirleyin.")

if len(parola) != 6 :
    print("Parolanız 6 karakterden oluşmalıdır. Tekrar deneyin.")
else :
    print("Hesabınız başarıyla oluşturuldu.")