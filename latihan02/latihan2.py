print('|Program Menampilkan Bilangan Terbesar ')
print('')

a = 1
max = 0
while a != 0:
    if a > max:
        max = a
    a = int(input('Masukkan bilangan :'))
    if a == 0:
        break

print(' Hasil Nilai Terbesar adalah :', max)
