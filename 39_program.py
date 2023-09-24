#39) Python program to check whether a string is Palindrom or Not
def fu(string):
    cl = string.replace(" ", "").lower()
    re = cl[::-1]

    if cl == re:
        return True
    else:
        return False

user_input = input("Enter a string: ")

if fu(user_input):
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")

    