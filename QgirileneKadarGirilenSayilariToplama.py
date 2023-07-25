print("Girilen sayılari toplama ve Q ile çıkma")

toplam=0

while True:
    sayi = input("Sayiyi giriniz")
    if(sayi=="q"):
        break
    else:
        sayi=int(sayi)
        toplam=toplam+sayi
print(toplam)