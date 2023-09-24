#23) Python program to find numbers divisible by another number

n=int(input("enter the number"))
div=[]
for x in range(1,n+1):
    if n%x==0:
        div.append(x)
print(f"this is given number {n} and output is {div}")
        
