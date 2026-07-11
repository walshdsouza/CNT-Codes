while True:
    print("Choose one:")
    print("1.Linear Congurential Generator")
    print("2.Blum Blum Shub")
    print("0.Exit")
    choice=int(input("Enter your choice:"))

    if choice==0:
        print("Exiting....")
        break
    elif choice==1:
    
        m=int(input("Enter mondulus(m): "))
        a=int(input("Enter multiplier(a)(0<=a<m): "))
        b=int(input("Enter adder(b)(0<=b<m): "))
        x0=int(input("Enter seed(x0)(0<=x0<m): "))
        n=int(input("Enter number of outputs(n): "))

        for i in range(n):
            x1=(a*x0+b)%m
            print(f"Output {i+1}: {x1}")
            x0=x1

    elif choice==2:
        p=int(input("Enter prime number p: "))
        q=int(input("Enter prime number q: "))
        x0=int(input("Enter seed(x0)(gcd(x0,m)=1): "))
        num=int(input("Enter number of outputs(n): "))

        m=p*q
        for i in range(num):
            x1=(x0**2)%m
            print(f"Output {i+1}: {x1}")
            x0=x1
             
