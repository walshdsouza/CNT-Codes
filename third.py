
print("Enter the values of a,b and c in ax+by=c:")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
r1 = a
r2 = b

s1 = 1
s2 = 0

t1 = 0
t2 = 1

print("\nExtended Euclid Algorithm")
print("-" * 65)
print(f"{'q':<6}{'r1':<8}{'r2':<8}{'r':<8}{'s1':<8}{'s2':<8}{'t1':<8}{'t2':<8}")
print("-" * 65)

while r2 != 0:
    q = r1 // r2
    r = r1 % r2

    s = s1 - s2 * q
    t = t1 - t2 * q

    print(f"{q:<6}{r1:<8}{r2:<8}{r:<8}{s1:<8}{s2:<8}{t1:<8}{t2:<8}")

    r1 = r2
    r2 = r

    s1 = s2
    s2 = s

    t1 = t2
    t2 = t

print("-" * 65)
print(f"GCD({a}, {b}) = {r1}")
print(f"s = {s1}")
print(f"t = {t1}")


x=a/r1
y=b/r1
z=c/r1
print("Particular Solution is:")
print(f"{x}*{s1} + {y}*{t1} = {z}")

x0=z*s1
y0=z*t1
print("General Solutions are:")
print("For x:")
print(f"x={x0}+k*{b}/{r1}")
print("For y:")
print(f"y={y0}-k*{a}/{r1}")
while True:
    print("Enter a choice:")
    print("1.Enter k value:")
    print("0.Exit")
    choice=int(input("Choice:"))

    if choice==0:
        print("Exiting....")
        break

    elif choice==1:
        k=int(input("Enter value of k:"))
        print("After putting value of k in general solution we get:")
        print("For x:")
        print(f"x={x0}+{k}*{y}")
        print("For y:")
        print(f"y={y0}-{k}*{x}")


