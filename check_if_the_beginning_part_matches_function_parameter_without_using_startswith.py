# ask user to input any word/s and the prefix
input_string = input("Enter any word/s: ")
prefix = input("Enter the prefix: ")
# check if the prefix matches the beginning of the string and print the output
if input_string[:len(prefix)] == prefix:
    print("True")
else:
    print("False")