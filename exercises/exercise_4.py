# write a program that takes a number and prints the full times table of that number do not include 0 

# take the user input 
user_input =  int(input("give me the number and i give you the times table "))
num  =int(user_input) 
x = list(range(1,num+1))
y = list(range(1,num+1))

rows, cols = (num, num) 
table = [[0 for i in range(cols)] for j in range(rows)] 

for elem_x in x :
    for elem_y in y:
        entry  = elem_x * elem_y
        table[elem_x-1][elem_y-1] = entry


for i in table: 
    print(str(i) + '\n')


     
