import math

n=int(input("Enter number of equations:"))
a_list=[]
m_list=[]
Mlist=[]
inv_list=[]
for num in range(1,n+1):
    print(f"Equation {num}:")
    a=int(input("Enter a:"))
    a_list.append(a)
    m=int(input("Enter m:"))
    m_list.append(m)

M=math.prod(m_list)
for num in range(1,n+1):
    calc_M=M//m_list[num-1]
    Mlist.append(calc_M)


for num in range(1,n+1):
    M1=Mlist[num-1]%m_list[num-1]
    y=1
    while(M1*y)%m_list[num-1]!=1:
        y+=1

    inv_list.append(y)


res=0
for num in range(1, n+1):
    res+=a_list[num-1]*Mlist[num-1]*inv_list[num-1]


result=res%M
print(f"Result of the system of equations is: {result}")


