while True:
    print("Select one:")
    print("1. Basic Math")
    print("2. Theorems")
    print("0. Exit")

    n=int(input("Enter your choice:"))

    if n==0:
        print("Exiting....")
        break

    if n==1:
        num1=int(input("Enter first number:"))
        num2=int(input("Enter second number:"))

        print("Select one:")
        print("1. Addition")
        print("2. Subtraction")    
        print("3. Multiplication")    
        print("4. Division")
        print("5. Remainder")
        print("6. Exponentiation")
        print("0. Exit")

        k=int(input("Enter choice:"))

        if k==0:
            print("Back to main menu.")
            continue

        if k==1:
            result=num1+num2
            print(f"Sum of {num1} and {num2} is: {result}") 

        if k==2:
            diff=num1-num2
            print(f"Difference of {num1} and {num2} is: {diff}")

        if k==3:
            mul=num1*num2
            print(f"Product of {num1} and {num2} is: {mul}")  

        if k==4:
            quo=num1//num2
            print(f"Quotient of {num1} divided by {num2} is: {quo}")

        if k==5:
            rem=num1%num2
            print(f"Remainder of {num1} divided by {num2} is: {rem}")

        if k==6:
            expo=num1**num2
            print(f"Result of {num1} raised to {num2} is: {expo}") 

    if n==2:
        num1=int(input("Enter first number:"))
        num2=int(input("Enter second number:"))
        num3=int(input("Enter third number:"))
        print("Choose one:")
        print("1. Theorem1:")
        print("2. Theorem2:")
        print("0. Exit")

        t=int(input("Enter your choice:"))

        if t==0:
            print("Back to main menu...")
            continue

        if t==1:
            if (num1%num2==0 and num2%num3==0):
                print(f"{num1} modulo {num3} is equal to 0")
                print("Theorem holds")
            else:
                print("Theorem not satisfied")

        if t==2:
            a=int(input("Enter num 1: "))
            b=int(input("Enter num 2: "))

            if (num1%num2==0 and num2%num3==0):
                print(f"{num1} modulo ( {num2}*{a}+{num3}*{b} ) is equal to 0")
                print("Theorem holds")
            else:
                print("Theorem not satisfied")



