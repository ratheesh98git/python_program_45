n=int(input("enter the number a"))
p=int(input("enter the number of b"))
temp=0

def ku(n,p):
    temp=n
    n=p
    p=temp
    return n,p

s,e=ku(n,p)

print(f"this is before swap {n}{p} after{s},{e}")