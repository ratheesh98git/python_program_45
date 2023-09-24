#40)Python program to remove punctuations from a string

input_string = "Hello, World! This is a test string with some punctuations."

punctuation_marks = '''!()-[]{};:'"\,.,'''

result=""
for ch in input_string:
    if ch not in punctuation_marks:
        result=result+ch
        
print("this is original string",input_string)
print("this is output string",result)