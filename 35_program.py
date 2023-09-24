#35) Python program to convert decimal to binary using recursion
def conv(n):
    if n==0:
        return 0
    elif n>1:
         conv(n//2)
    print(n%2,end="")
n=int(input("enter the number"))
conv(n)