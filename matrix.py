import os

os.system('clear')

print("-----------------------------------------------")
print("               Program Matrix")
print("-----------------------------------------------")

matrix = []
ukuran_baris = input("Masukkan banyak baris matrix : ")
ukuran_kolom = input("Masukkan banyak kolom matrix : ")

print("-----------------------------------------------")
print("Program ini akan membuat matrix", ukuran_baris + "x" + ukuran_kolom + ".")
print("-----------------------------------------------")

for baris in range(int(ukuran_baris)) :
    a = []

    for kolom in range(int(ukuran_kolom)) :
        print("  - Masukkan nilai matrix di", str(int(baris + 1)) + "x" + str(int(kolom) + 1), ": ", end='')
        a.append(int(input()))

    matrix.append(a)

print("===============================================")

print("Berikut matrix kamu : ")
for baris in range(int(ukuran_baris)) :
    print("       ", end="")
    for kolom in range(int(ukuran_kolom)) :
        print(matrix[baris][kolom], end='   ')
    print()

print("===============================================")


