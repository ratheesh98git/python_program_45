#26) Python program to find HCF and GCD


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if n1 > n2:
    smaller = n2
else:
    smaller = n1

gcd = 1  # Initialize gcd to 1 before the loop

for i in range(1, smaller + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i  # Update gcd when a common divisor is found

print("The GCD of", n1, "and", n2, "is", gcd)
