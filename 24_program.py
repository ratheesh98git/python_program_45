#24) Python program to convert decimal to binary, octaland hexadecimal

decimal_num = int(input("Enter a decimal number: "))

binary=bin(decimal_num)
octal=oct(decimal_num)
hexa=hex(decimal_num)

print(f"decimal_numb:{decimal_num}")
print(f"binary:{binary}")
print(f"octal:{octal}")
print(f"hexadecimal:{hexa}")