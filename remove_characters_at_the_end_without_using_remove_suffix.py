# ask user to input any word/s and a suffix
input_string = input("Enter any word/s: ")
suffix = input("Enter a suffix: ")
# print the output if the string ends with the suffix
if input_string.endswith(suffix):
    print(input_string[:-len(suffix)])
else:
    print(input_string)