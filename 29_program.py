#29) Python program to make a simple calculator
print("press 1 is addition")
print("press 2 is substraction")
print("press 3 is multiplication")
print("press 4 is division")


n=int(input("enter the choice(1,2,3,4) : "))
if n==1:

  def ad(x,y):
      return x+y
elif n==2:

  def su(x,y):
    return x-y
elif n==3:

  def mul(x,y):
    return x*y
elif n==4:

   def div(x,y):
        if y!=0:
            return x/y
        else:
            return "zero division error"    
if n>4:
    print("your enter the out of range")    
if  n in[1,2,3,4]:
    x = float(input("Enter the first number (x): "))
    y = float(input("Enter the second number (y): "))
    if n==1:
        result=ad(x,y)
    elif n==2:
        result=su(x,y)
    elif n==3:
        result=mul(x,y)
    elif n==4:
        result=div(x,y)
    print("result",result)
print("thank you for using")