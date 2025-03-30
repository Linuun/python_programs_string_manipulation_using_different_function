# ask user to input any words and the space they want
input_string = input("Enter any word/s: ")
space_characters = int(input("Enter the number of space characters you want: "))
# calculate the number of space characters to add to the left
total_spaces = space_characters - len(input_string)
if total_spaces <= 0:
    print(input_string)
# print the output
else:
    print(" " * total_spaces + input_string)