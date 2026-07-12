def euclid_algorithm(a, b):
    r1 = a
    r2 = b

    print("\nEuclid Algorithm")
    print("-" * 33)
    print(f"{'q':<8}{'r1':<8}{'r2':<8}{'r':<8}")
    print("-" * 33)

    while r2 != 0:
        q = r1 // r2
        r = r1 % r2

        print(f"{q:<8}{r1:<8}{r2:<8}{r:<8}")

        r1 = r2
        r2 = r

    print("-" * 33)
    print(f"GCD({a}, {b}) = {r1}")


def extended_euclid(c, d):
    r1 = c
    r2 = d

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
    print(f"GCD({c}, {d}) = {r1}")
    print(f"s = {s1}")
    print(f"t = {t1}")


while True:

    print("\nChoose one:")
    print("1. Euclid Algorithm")
    print("2. Extended Euclid Algorithm")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Exiting...")
        break

    elif choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        euclid_algorithm(a, b)

    elif choice == 2:
        c = int(input("Enter first number: "))
        d = int(input("Enter second number: "))
        extended_euclid(c, d)

    else:
        print("Invalid choice!")