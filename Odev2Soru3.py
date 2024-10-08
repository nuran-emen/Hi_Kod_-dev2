while True :
    parola = input("Lütfen 5 ile 10 karakter arasında bir parola girin :")
    if 5 <= len(parola) <= 10 :
        print("Hesabınız başarıyla oluşturuldu.")
        break 
    else :
        print("Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!")