"""Samet TAŞCI - 234210076
Kriptoloji Proje Ödevi"""

import hashlib


def hash_olustur(metin, algoritma):
    if algoritma == 'md5':
        return hashlib.md5(metin.encode()).hexdigest()
    elif algoritma == 'sha1':
        return hashlib.sha1(metin.encode()).hexdigest()
    elif algoritma == 'sha256':
        return hashlib.sha256(metin.encode()).hexdigest()
    else:
        return None


def hash_karsilastir(metin, verilen_hash, algoritma):
    olusturulan_hash = hash_olustur(metin, algoritma)
    return olusturulan_hash == verilen_hash


def main():
    print("Hash İşlemleri")
    print("1. Hash Oluşturma")
    print("2. Hash Karşılaştırma")
    secim = input("Lütfen bir işlem seçin (1/2): ")

    if secim == '1':
        metin = input("Hashlenecek metni girin: ")
        print("Algoritma seçenekleri: md5, sha1, sha256")
        algoritma = input("Kullanılacak algoritmayı seçin: ")

        sonuc = hash_olustur(metin, algoritma)
        if sonuc:
            print(f"Oluşturulan hash ({algoritma}): {sonuc}")
        else:
            print("Geçersiz algoritma seçimi!")

    elif secim == '2':
        metin = input("Hash'i karşılaştırılacak metni girin: ")
        verilen_hash = input("Karşılaştırılacak hash'i girin: ")
        print("Algoritma seçenekleri: md5, sha1, sha256")
        algoritma = input("Kullanılacak algoritmayı seçin: ")

        if hash_karsilastir(metin, verilen_hash, algoritma):
            print("Girilen metin, verilen hash ile eşleşiyor.")
        else:
            print("Girilen metin, verilen hash ile eşleşmiyor.")

    else:
        print("Geçersiz seçim yaptınız!")


if __name__ == "__main__":
    main()
