#21) Python program to find the sum of natural numbers


n=int(input("enter the number"))

if n<0:
    print("ente the positive number")
else:
    sum=0
    while n>0:
        sum=sum+n
        n=n-1
print("this is sum of natural number",sum)
        