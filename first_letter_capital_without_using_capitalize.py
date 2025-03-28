# ask user to input any word/s but the first letter is in lower case
input_string = input("Enter any word/s (first letter in lower case): ")
# print the output using upper and lower function
print(input_string[0].upper() + input_string[1:].lower())