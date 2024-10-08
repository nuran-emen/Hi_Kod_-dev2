maas = float(input("Maaş miktarını girin:"))

if maas<10000 :
    print("Vergi miktarı :", maas*0.05)
    print("Yeni maaş miktarınız:",maas*0.95)
elif maas<25000:
    print("Vergi miktarı :", maas*0.1)
    print("Yeni maaş miktarınız:",maas*0.9)
elif maas<45000 :
    print("Vergi miktarı :", maas*0.25)
    print("Yeni maaş miktarınız:",maas*0.75)
else :
    print("Vergi miktarı :", maas*0.3)
    print("Yeni maaş miktarınız:",maas*0.7)