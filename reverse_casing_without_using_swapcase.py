# ask user to input words in improper casing
input_string = input("Enter any words (in improper casing): ")
# initialize a variable for storing characters
swapcase = ""
# use for loop
for letter in input_string:
# check if the character is in upper case then add its lower case into the variable
    if letter.isupper():
        swapcase += letter.lower()
# check if the character is in lower case then add its upper case into the variable
    else:
        swapcase += letter.upper()
# print the output
print(swapcase)