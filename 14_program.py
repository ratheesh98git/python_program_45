#14) Python program to check prime number


n=int(input("enter the number"))

if n==1:
    print("it's not a prime number")

if n>1:
    for x in range(2,n):
        if n%2==0:
            print("it's not a prime number")
            break
    else:
        print(n,"it's prime number")
            
