n=int (input("Enter the number: "))
count=0
num=(n+count**2)**0.5
while(num%1!=0):
    count+=1
    num=(n+count**2)**0.5

a=num+count
b=num-count

print(f"The factors of {n} are: {a} and {b}")
