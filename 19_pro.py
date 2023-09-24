n = int(input("enter the number"))
temp=n
tot=0

while n>0:
    d=n%10
    tot=tot+(d*d*d)
    n=n//10
    print(tot)
if temp==tot:
    print("yes it's astronomy")
else:
    print("it's not  astronomy")