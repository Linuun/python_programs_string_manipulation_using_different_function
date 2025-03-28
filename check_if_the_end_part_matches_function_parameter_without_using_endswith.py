# ask user to input any word/s and the suffix 
input_string = input("Enter any word/s: ")
suffix = input("Enter the suffix: ")
# check if the length of suffix is greater than the string
if len(suffix) > len(input_string):
    print("False")
# print the output by comparing the end of the string with the suffix
print(input_string[-len(suffix): ] == suffix)