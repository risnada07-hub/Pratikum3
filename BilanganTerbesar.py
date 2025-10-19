# Input dua bilangan dari pengguna
a = float(input("Masukkan bilangan pertama: "))
b = float(input("Masukkan bilangan kedua: "))

# Menentukan bilangan terbesar
if a > b:
    print(f"Bilangan Terbesar Adalah Bilangan {a}")
elif b > a:
    print(f"Bilangan Terbesar Adalah Bilangan {b}")
else:
    print(f"Kedua bilangan sama besar: {a} & {b}")
