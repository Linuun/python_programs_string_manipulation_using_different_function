# ask user to input any word/s
input_string = input("Enter any word/s: ")
# use while loop and remove the spaces at the end of the string
while input_string and input_string[-1] == " ":
    input_string = input_string[:-1]
# print the output