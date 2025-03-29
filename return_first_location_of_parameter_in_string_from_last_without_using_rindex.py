# ask user to input any word/s and the string they want to locate
input_string = input("Enter any word/s: ")
sub_string = input("Enter the string you want to locate: ")
# print Error if the string was not found in the input
if sub_string not in input_string:
    print("Error: string not found")
# print the output using rfind function
else:
    print(input_string.rfind(sub_string))