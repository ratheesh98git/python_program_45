#15) Python program to print all prime numbers in an interval

lower=int(input("enter the number"))
upper=int(input("enter the upper number"))

for x in range(lower,upper+1):
    if x>1:
        for p in range(2,x):
            if x%2==0:
                break
        else:
            print(x)