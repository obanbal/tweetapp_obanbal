simgegir = input("Bir roma rakamı giriniz: ")

romarakamlari = {
    'I': 1, 'V': 5, 'X': 10,
    'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

def gecerli_roma_rakami(sayi):
    # Geçerlilik kontrolü
    for rakam in sayi:
        if rakam not in romarakamlari:
            #print("Girdiğiniz sembol bir roma rakamı değildir!")
            return False # Geçersiz sembol varsa False döndür

    # 3'ten fazla tekrarı kontrol et
    for rakam in romarakamlari:
        if sayi.count(rakam) > 3:
            print("Aynı simge 3 defadan fazla yanyana girilmiştir. Bu kural dışıdır.")
            return False

    # Girilen simgelerin değerini hesaplama
    toplam = 0
    ilk_deger = 0

    for rakam in reversed(sayi):
        deger = romarakamlari[rakam]
        if deger < ilk_deger:
            toplam -= deger
        else:
            toplam += deger

        ilk_deger = deger # Geçerli ise toplam değeri döndür
    return toplam # Geçerli ise toplam değeri döndür

toplam = gecerli_roma_rakami(simgegir)
if toplam is not False:
    print(f"{simgegir} Geçerli bir Roma rakamıdır. Değeri de {toplam}")
else:
    print("Geçerli bir Roma rakamı değildir.")
