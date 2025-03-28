# ask user to input any word/s and a prefix
input_string = input("Enter any word/s: ")
prefix = input("Enter a prefix: ")
# print the output if the string starts with the prefix
if input_string.startswith(prefix):
    print(input_string[len(prefix):])
else: 
    print(input_string)