#27) Python program to find LCM
n1=int(input("enter the number"))
n2=int(input("enter the number 2"))

if n1>n2:
    greater=n1
else:
    greater=n2
while(True):
    if greater%n1==0 and greater%n2==0:
        lcm=greater
        break
    greater+=1
print(f"this is given number {n1},{n2}, and output {lcm}")