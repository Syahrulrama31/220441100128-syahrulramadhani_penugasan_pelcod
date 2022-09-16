from operator import index
from tkinter import Menu


menu = {
    "c": "celcius to fahrenhit ",
    "f": "fahrenheit to kelvin",
}

print("======pilih menu satuan skala suhu======")
for i in menu:
    print("satuan suhu :", i, "\t menu : ", menu[i])

suhu = float(input("Masukkan nilai suhu : "))
satuan = input("masukkan pilihan menu :")

if (satuan == "c"):
    print("Hasil dari", suhu, "Derajat Celcius To Fahrenheit =",
          (suhu*9/5)+32, "Derajat")
elif (satuan == "f"):
    print("Hasil dari", suhu, "Fahrenhait To Kelvin =",
          (suhu-32)*(5/9)+273, "Derajat")
