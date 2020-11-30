# create a function that when given two strings of letters determins whether the second can be made from 
# the first by removing one letter the remaining letters must stay in the same order 

 #can the second string be made from removing a letter from the first string 
import copy
def stringtest(string_1,string_2):
# loop through string 2 and remove each letter and compare to string 1 
    index = 0
    str_2_list = list(string_2)
   
    while index < len(string_2):
        #remove from list 
        comparitor_list = copy.copy(str_2_list)
        comparitor_list.pop(index)
        comparitor_str =  "".join(comparitor_list)
        if (comparitor_str == string_1):
            return True 
        
        index = index +1

    return False
    
print(str(stringtest("rest","reset")))
