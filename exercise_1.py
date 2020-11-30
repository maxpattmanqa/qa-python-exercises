#SBN's (International Standard Book Numbers) are identifiers for books.
#The ISBN is a thirteen-digit code.
#The last digit is a check number calculated as follows:
#The first 12 digits are taken
#Starting at index 0, if the index is even - add it, and if the index is odd – multiply the digit by three then add it.
#From the sum find the remainder after dividing by 10.
#10 minus the remainder give us the check digit
#In other words the following algebra would give us the check digit:
#digit_12 = 10 – (( digit_0 + (3 x digit_1) + digit_2 + (3 x digit_3) + digit_4 + (3 x digit_5) + digit_6 + (3 x digit_7) + digit_8 + (3 x digit_9) + digit_10 + (3 x digit_11) ) % 10)

user_input = input("Enter 12 numbers separated by '-' : ")

input_list = user_input.split('-')
numbers = [int(x.strip()) for x in input_list]

output_list = []
index = 0
for x in numbers:
    #if even 
    if index %2 == 0:
        output_list.append(str(x))

    else: 
        x2 = int(x)
        x2 = (x2*3)
        output_list.append(str(x2))

    index+= 1

print(output_list)
    