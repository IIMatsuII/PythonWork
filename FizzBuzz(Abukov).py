#This program was written by Abukov Rustam for his GitHub
n = int(input())

for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print("AbukovRustam")
#This string can be changed in order to change it to apply only to odd numbers
    elif x % 2 == 0:
        continue
    elif x % 3 == 0:
        print("Abukov")
    elif x % 5 == 0:
        print("Rustam")
    else:
        print(x)