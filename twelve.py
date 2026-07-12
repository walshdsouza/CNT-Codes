q=int(input("Enter q value:"))
a=int(input("Enter a value:"))
Xa=int(input("Enter user A's private key(Xa):"))
Xb=int(input("Enter user B's private key(Xb):"))

Ya=(a**Xa)%q
Yb=(a**Xb)%q

print(f"User A's public key is: {Ya}")
print(f"User B's public key is: {Yb}")

print("Verification after exchanging public keys:")
ka=(Yb**Xa)%q
kb=(Ya**Xb)%q
print(f"User A's verification result is (ka): {ka}")
print(f"User B's verification result is (kb): {kb}")

if ka==kb:
    print("Verification successful! Values match.")
else:
    print("Verification failed! Values do not match.")    
