#16) Python program to find the factorial of a number


n=int(input("enter the number"))

factorial=1

if n<0:
    print("enter the positive number")
elif n==0:
    print("this is zero so enter the rigtht number")
    
else:
    for x in range(1,n+1):
        factorial=factorial*x
    print("this is factorial number",n, "is",factorial)
    