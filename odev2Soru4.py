dogru_isim = "kullanici"
dogru_sifre = "123456"

isim = input("Kullanıcı adınızı girin:")

if isim == dogru_isim :
    for hak in range(3,0,-1):
        sifre = input("Parolanızı girin :")
        
        if sifre == dogru_sifre :
            print("Giriş yapıldı.")
            break
        
        else :
            if hak-1 > 0 :
                print(f"Yanlış şifre girildi! {hak-1} deneme hakkınız kaldı.")
            else :
                print("Deneme hakkınız kalmadı!")
                
else :
    print("Kullanıcı bulunamadı.")