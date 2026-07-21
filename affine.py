import math
str=input("Enter the string: ")
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
print("Choose one:")
print("1. Encrypt")
print("2. Decrypt")
choice=int(input("Enter your choice: "))
if choice==1:
    encrypted=""
    for i in str:
        if i.isalpha():
            if i.isupper():
                encrypted+=chr(((ord(i)-65)*a+b)%26+65)
            else:
                encrypted+=chr(((ord(i)-97)*a+b)%26+97)
        else:
            encrypted+=i
    print(f"The encrypted string is: {encrypted}")

if choice==2:
    a1=pow(a,-1,26)
    decrypted=""
    for i in str:
        if i.isalpha():
            if i.isupper():
                decrypted+=chr((a1*(ord(i)-65-b))%26+65)  
            else:
                decrypted+=chr((a1*(ord(i)-97-b))%26+97)
        else:
            decrypted+=i
    print(f"The decrypted string is: {decrypted}")  