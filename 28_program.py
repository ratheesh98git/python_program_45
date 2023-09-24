#28) Python program to find the factors of a number

n=int(input("enter the number"))

for x in range(1,n+1):
    if n%x==0:
        print(x)