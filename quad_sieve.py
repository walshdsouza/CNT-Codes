import math
n=int(input("Enter the number: "))
start=math.isqrt(n)
for i in range (start, start+100):
    value=(i*i)%n
    b=math.isqrt(value)
    if b*b==value:
        a=i
        result=math.gcd(a-b,n)
        if result!=1 and result!=n:
            print(f"The factors of {n} are: {result} and {n//result}")
            break

        


