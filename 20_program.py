#20) Python program to find Armstrong number in an interval
lower=int(input("enter the lower number"))
upper=int(input("enter the upper number"))

for  n in range(lower,upper+1):
    tot=0
    x=n
    while x>0:
        d=x%10
        tot=tot+d*d*d
        x//=10
    if tot==n:
        print(n, end=" ")
        