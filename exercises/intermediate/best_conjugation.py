import urllib.request

# read text from the url link 

#http://www-personal.umich.edu/~jlawler/wordlist
#user_input = input("Please Enter a word to Receive sub-words")

def retreive_word_bank(url_address):
    fp = urllib.request.urlopen(url_address)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    word_bank = [x.strip() for x in mystr.split()]
    return word_bank


def best_conjugation():
    user_input = input("enter a word you would like to see the sub words of")
    word = user_input
    word_bank = retreive_word_bank('http://www-personal.umich.edu/~jlawler/wordlist')
#we can print all the words on the site 
    output_string = ''
# go through user string and check with the list if that substring is contained within the list add to final string 

    window_L = int(0)
    window_R = int(1)
    while window_L <= len(word):
        while window_R <= len(word):  
            substring = word[window_L:window_R]
            if str(substring) in word_bank:
                output_string = (output_string + substring + ' ,')
            window_R+=1 
        window_L+=1
        window_R=window_L+1
    
    return output_string



print(best_conjugation())