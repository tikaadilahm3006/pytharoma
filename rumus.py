def hitung_luas_segitiga (alas,tinggi):
    return 0.5 * alas *tinggi

def hitung_luas_persegi (panjang_sisi):
    return panjang_sisi ** 2

def hitung_luas_lingkaran (jari_jari):
    return 3.14 * jari_jari ** 3

def hitung_luas (menu, *args):
    if menu == 1:
        return hitung_luas_segitiga(*args)
    elif  menu == 2:
        return hitung_luas_persegi(*args)
    elif menu == 3:
        return hitung_luas_lingkaran(*args)
    else:
        return "Menu tidak valid"