while(True):
    print("RSA Algorithm Implementation Menu:")
    print("1.Calculate RSA")
    print("2.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("RSA Algorithm Implementation")
        p=int(input("Enter a prime number p: "))
        q=int(input("Enter a prime number q: "))
        n=p*q
        phi=(p-1)*(q-1)
        
        e=int(input("Enter e value:"))
        if e<=1 or e>=phi:
            print("Invalid e value. It must be greater than 1 and less than phi.")
            continue
        else:
            d=pow(e,-1,phi)
            print(f"Public key (e, n): ({e}, {n})")
            print(f"Private key (d,n): ({d}, {n})")
            pt=int(input("Enter plaintext (as an integer): "))
            ct=(pt**e)%n
            print(f"Encryption: {ct}")
            dt=(ct**d)%n
            print(f"Decryption: {dt}")
    elif choice==2:
        print("Exiting...")
        break

        

