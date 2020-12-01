from num2words import num2words

# Piggy backing off the no repeat principle this is a very cheeky solution 
user_input = input("Please enter a number: ")
print(str(num2words(user_input)))
