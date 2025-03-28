# ask user to input words but first letter are in lower case
input_string = input("Enter any words (first letter should be in lower case): ")
# print the output by capitalizing every first letter using split, capitalize, and join fucntion
print(" " .join(word.capitalize() for word in input_string.split()))