#34) Python program to find factorial of number using recursion

def fac(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*fac(n-1)
n=int(input("enter the number"))
print(fac(n))
    