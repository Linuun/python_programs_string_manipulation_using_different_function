# ask user to input any word and the number of space characters they want
input_string = input("Enter any word/s: ")
space_characters = int(input("Enter the number of space characters you want: "))
# calculate the total number of space characters
total_spaces = space_characters - len(input_string)
if total_spaces <= 0:
    print(input_string)
# calculate the number of space characters to add in left and right
left_spaces = total_spaces // 2
right_spaces = total_spaces - left_spaces
# print the output
print(" " * left_spaces + input_string + " " * right_spaces)