import math
def value(number):
    result=(number*number)+1
    return result

n=int(input("Enter the number: "))
x0=2
y0=2
while(True):
    x0=value(x0)%n
    y0=value(value(y0)%n)%n
    result=math.gcd(abs(x0-y0),n)
    if result!=1 and result!=n:
        break

print(f"The factors of {n} are: {result} and {n//result}")


    