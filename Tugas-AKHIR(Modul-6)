def faktorial(x):
  angka = 1
  for i in range(1,x+1):
    angka *= i
  return angka
n = int(input("Masukkan n-nya : "))
r = int(input("Masukkan r-nya : "))
b = n - r
print("{}P{} = {}".format(n,r,faktorial(n)/faktorial(b)))
print("{}C{} = {}".format(n,r,faktorial(n)/(faktorial(b)*faktorial(r))))


def deretKonvergen(n,N):
counter = 1
total = 0
penyebut = 1
while(counter<= N):
x = n/penyebut
print("{}/{}".format(n,penyebut), end = " ")
if counter %2 == 0 :
total -= x
if counter !=N :
print("+", end = " ")
else:
total += x
if counter != N :
print("-", end = " ")
penyebut += 2
counter += 1
print("= {}".format(total))
n = int(input("Masukkan banyaknya suku n : "))
N = int(input("Masukkan banyak
