# ask user to input a string in lowercase
input_string = input("Enter any word/s (in lowercase): ")
# initialize a variable to store the letters
result = ""
# use for loop
for letter in input_string:
# check if the letter is in lowercase
# add the capitalized letter to the variable
    if letter.islower():
        result += letter.capitalize()
    else:
        result += letter
# print the output