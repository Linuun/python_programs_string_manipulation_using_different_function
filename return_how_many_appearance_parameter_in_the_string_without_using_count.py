# ask user to input any word/s and the character/s they want to count
input_string = input("Enter any word/s: ")
sub_string = input("Enter the character you want to count the number of appearance: ")
# initialize a variable for count and start
count = 0
start = 0
# use while loop
while start < len(input_string):
# find the position of the character starting from "start" index
    position = input_string.find(sub_string, start)
# check if the character is found in the string, add 1 to the count and update the start position
    if position != 1:
        count += 1
        start = position + 1
# break the loop
    else:
        break
# print the output