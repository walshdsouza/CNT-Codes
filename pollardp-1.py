import math
n = int(input("Enter the number: "))
bound=int(input("Enter the bound: "))
flag=0
for i in range(1, bound+1):
    result=math.gcd((2**i)-1, n)
    if result!=1:
        flag=1
        break

if flag==1:
    print(f"The factors of {n} are: {result} and {n//result}")
else:
    print(f"No factors found for {n} within the bound {bound}.")    
