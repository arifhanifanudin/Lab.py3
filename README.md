# Latihan01

Alur Agoritmanya :

a) import random memanggil file random

b) n = int(input("Masukan nilai N : ")) input variabel n, tipe data integer

c) for i in range(n) : looping for, dengan jumlah perulangan sebanyak n

d) a=random.uniform(0.0,0.5) variabel a berisikan random angka dari 0.0 sampai 0.5

e) print ("data ke : ", i, "=> ", a) print data ke : i = index looping a = angka random sesuai syarat nomer 4

f) print("Selesai") 

# flowchart

![img](https://user-images.githubusercontent.com/43899133/52893529-cc793e80-31cf-11e9-9c59-c11bd905c0d6.png)

# Syntax PYTHON

print('Program Menampilkan Nilai Bilangan Acak Lebih < 0.5')

print('')

import random

n = int(input("Masukan nilai N : "))

for i in range(n) :

    a=random.uniform(0.0,0.5)
    print ("Data ke : ", i, "=> ", a)
    
print("Program Selesai")

# Fotp hasil

![img](https://raw.githubusercontent.com/arifhanifanudin/Lab.py3/master/latihan01/hasil1.PNG)

# Latihan02

Alur Algoritmanya :
  
a) a=1 //variable a diisi 1, agar bisa masuk ke syarat while max=0 //variable max diisi 0

b) while a!=0 : looping while dengan syarat a bukan 0

c) if x > max : max = a proses if untuk mencari nilai terbesar

d) a = int(input("Masukan bilangan : ")) input nilai a dengan tipe data integer

e) if a == 0 : break jika inputan a diisi angka 0 maka break alias berhenti looping

f) print("Bilangan terbesar adalah : ",max) print nilai terbesar, variabel max

# flowchart

![img](https://user-images.githubusercontent.com/43899133/52893530-d00cc580-31cf-11e9-9359-106996608278.png)
 
# Syntax PYTHON

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

# Foto hasil

![img](https://raw.githubusercontent.com/arifhanifanudin/Lab.py3/master/latihan02/Hasil2.PNG)

# Program 1

Alur Agoritmanya :

a) x=100000000 modal 100,000,000, variable x

b) sum=0 variable untuk menjumlah total laba

c) y=0 variable untuk masa bulan

d) lb = [int(0), int(0), int(x) * .1, int(x) * .1, int(x) * .5, int(x) * .5, int(x) * .5, int(x) * .2]

*variable untuk jumlah laba perbulan,

dipisahkan dengan koma, tipe data integer

e) for i in lb : looping for indexs i, dengan mengambil data dari lb

f) sum=sum+i rumus untuk menghitung total laba perbulan

g) y+=1 masa bulan, tiap looping menambah 1

h) print("laba bulan ke-", y ,"sebesar :", i ) print : y = ambil masa bulan, i = ambil dari data yg ada di dalam lb

i) print("Total laba adalah :", sum) print total laba

# flowchart

![img](https://user-images.githubusercontent.com/43899133/52893531-d26f1f80-31cf-11e9-81f9-3af17a891615.png)

# Syntax PYTHON

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

# Foto hasil

![img](https://raw.githubusercontent.com/arifhanifanudin/Lab.py3/master/Program1/Ftprogram1.PNG)
