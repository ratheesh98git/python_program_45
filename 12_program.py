#12) Python program to check leap year

n=int(input("enter the number"))

if(n%4==0 and n%100!=0) or( n%400==0):
    print("it's leap year")
else:
    print("it's not a leap year")
