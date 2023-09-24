#18) Python program to print the fibonacci sequence

nterms=int(input("enter the number"))
n1,n2=0,1
count=0
if nterms<=0:
    print("enter the positive number")
elif nterms==1:
    print("please enter the right number not a zero")
    print(n1)
else:
    print("fibonacic series up to n  terms")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1