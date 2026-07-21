def jacobi(a, n):
    """Calculates the Jacobi symbol (a/n)"""
    if n <= 0 or n % 2 == 0:
        return 0
    a = a % n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a = a // 2
            if n % 8 == 3 or n % 8 == 5:
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    if n == 1:
        return result
    return 0
while(True):
    n=int(input("Enter a number:"))
    if n%2==0:
        print(f"{n} is not a prime number.")
        break
    print(f"Primality Testing for {n}:")
    print("1.Fermat's Primality Test")
    print("2.Miller-Rabin Primality Test")
    print("3.Solovay-Strassen Primality Test")
    print("4.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Fermat's Primality test:")
        if (2**(n-1))%n==1:
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is not a prime number.")

    elif choice==2:
        print("Miller Rabin test:")
        s=n-1
        k=0
        while s%2==0:
            s=s//2
            k+=1
        m=s%2
        a=int(input(f"Enter a value for a(1<a<{n-1}):"))
        if a<=1 or a>=n-1:
            print(f"Invalid a value. It must be greater than 1 and less than {n-1}.")
            continue

        
        b=0
        
        if (a**m)%n==1:
            print(f"{n} is a composite number.")
            break
        else:
            b= (a**m)%n   
        flag=0
        while flag<k-1:
            b=(b**2)%n
            if b==1:
                print(f"{n} is a composite number.")
                break
            flag+=1
        
        if b==1:
            print(f"{n} is a composite number.")
        else:
            print(f"{n} is a prime number.")
    elif choice==3:
        print("Solovay Strassen Test:")
        
        # We will test using base a = 2 (as in your original code)
        # Note: A full implementation would test multiple random values of 'a'
        a = 2
        
        # Calculate LHS: a^((n-1)/2) mod n using efficient modular exponentiation
        lhs = pow(a, (n - 1) // 2, n)
        
        # Calculate RHS: The Jacobi symbol (a/n)
        rhs = jacobi(a, n)
        
        # In modular arithmetic, if the Jacobi symbol is -1, it maps to n - 1
        if rhs == -1:
            rhs = n - 1
            
        # Compare LHS and RHS
        if lhs == rhs and rhs != 0:
            print(f"{n} is a prime number (Probably).")
        else:
            print(f"{n} is a composite number.")
    elif choice==4:
        print("Exiting...")
        break     
    else:
        print("Invalid choice! Please try again.")                              

                    



