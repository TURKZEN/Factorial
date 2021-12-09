from math import * 
print("""

------------------------------
|    Factorial-Faktöriyel    |
|       Calculation          |
------------------------------
https://github.com/TURKZEN

""")

while True:
    a = input("Çıkmak istermisiniz ? (y/n)")
    if a == "q":
        break
    else:
        x = int(input("Sayıyı Giriniz : "))
        print(x,"! =",factorial(x))