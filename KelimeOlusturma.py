
from random import randint


def ilk_harfe_karar_ver():
    rastgeleSayi = randint(0, 1)
    if rastgeleSayi == 0:
        harfTuru = "sesli"
    elif rastgeleSayi == 1:
        harfTuru = "sessiz"
    return harfTuru


def hece_kac_harfli_olacak():
    heceninHarfSayisi = randint(1, 2)
    return heceninHarfSayisi


def tek_harfli_hece():
    # tek harfli heceler sadece sesli harften oluşabilir
    return(rasgele_harf_getir("sesli"))


def iki_harfli_hece(hecenin_ilk_harfinin_turu):
    if hecenin_ilk_harfinin_turu == "sesli":
        ilkHarf = rasgele_harf_getir("sesli")
        ikinciHarf = rasgele_harf_getir("sessiz")
    elif hecenin_ilk_harfinin_turu == "sessiz":
        ilkHarf = rasgele_harf_getir("sessiz")
        while ilkHarf == "ğ":
            ilkHarf = rasgele_harf_getir("sessiz")
        ikinciHarf = rasgele_harf_getir("sesli")
    ikiHarfliHece = ilkHarf + ikinciHarf
    return ikiHarfliHece


def rasgele_harf_getir(harfTuru):
    sesliHarfler = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    sessizHarfler = ["b", "c", "ç", "d", "f", "g", "ğ", "h", "j",
                     "k", "l", "m", "n", "p", "r", "s", "ş", "t", "v", "y", "z"]
    if harfTuru == "sesli":
        rastgeleSayi = randint(0, 7)
        return sesliHarfler[rastgeleSayi]
    elif harfTuru == "sessiz":
        rastgeleSayi = randint(0, 20)
        return sessizHarfler[rastgeleSayi]


def hece_olustur(heceninHarfSayisi):
    hece = ""
    if heceninHarfSayisi == 1:
        hece = tek_harfli_hece()
    elif heceninHarfSayisi == 2:
        heceninIlkHarfi = ilk_harfe_karar_ver()
        hece = iki_harfli_hece(heceninIlkHarfi)
    return hece


def kelime_olustur():
    kelime = ""
    heceler = list()
    hecelerinHarfSayisi = list()
    HeceSayisi = randint(1, 3)
    for hece in range(HeceSayisi):
        harfSayisi = hece_kac_harfli_olacak()
        hecelerinHarfSayisi.append(harfSayisi)
        
        hece = hece_olustur(harfSayisi)
        heceler.append(hece)
    kelime = kelime.join(heceler)
    return kelime


print(kelime_olustur())
