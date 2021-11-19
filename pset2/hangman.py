# Problem Set 2, hangman.py
# Name: Lamis Menghour
# Collaborators: 
# Time spent: 10 days

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import re
import os
os.system('cls' if os.name == 'nt' else 'clear')
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

Vowels=['a','e','i','o']
letters_guessed = []

"""
for i in range(X):
    charcter = input('Please guess a letter:')
    letters_guessed.append(charcter) 
print('Letters have been guessed :', letters_guessed)
"""


#Python program to convert a list to string    
def listToString(letters_guessed): 
    
    # initialize an empty string
    l_g = "" 
    
    # traverse in the string  
    for element in letters_guessed: 
        l_g += element  
    
    # return string  
    return l_g 

#listToString(letters_guessed)       
 

def is_word_guessed(secret_word, letters_guessed):
    for i in range(X):
        charcter = input('Please guess a letter:')
        letters_guessed.append(charcter) 
    is_word_guesse= all (letters in secret_word for letters in letters_guessed)
    print(is_word_guesse)

#is_word_guessed(secret_word, letters_guessed)


def get_guessed_word(secret_word, letters_guessed):
    for i in range(X):
        charcter = input('Please guess a letter:')
        letters_guessed.append(charcter) 
    get_guesse= ''
    for ltr in secret_word:
        if (ltr in letters_guessed ):
            get_guesse += ltr 
        else:
            get_guesse += '_ '

    print('Letters have been guessed true : ', get_guesse)

#get_guessed_word(secret_word, letters_guessed)

def get_available_letters(letters_guessed):
    for i in range(X):
        charcter = input('Please guess a letter:')
        letters_guessed.append(charcter) 
        for charcter in letters_guessed:
            if (charcter in string.ascii_lowercase) :
                index = string.ascii_lowercase.index(charcter) 
                string.ascii_lowercase  = string.ascii_lowercase[ :index] +  string.ascii_lowercase[index+1 : ]

    print('Available_letters :  ' , string.ascii_lowercase)

# get_available_letters(letters_guessed)

#print('------------------------')

def hangman(secret_word):
    #print(secret_word)
    X = len(secret_word)
    guesses = 6
    warnings = 3 

    get_guesse_list=[]
    for i in range(X):
        get_guesse_list.append("_ ")

    S=listToString(get_guesse_list)

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ', X ,' letters long.')
    print('You have ', warnings ,' warnings left')
    print('------------------------')

    while guesses > 0 :
        print('You have ', guesses ,' guesses left')
        print('Available_letters :  ' ,string.ascii_lowercase)

        charcter = input('Please guess a letter :') 
        if str.islower(charcter) is False :
            charcter=charcter.lower()

        if str.isalpha(charcter) is True and str.islower(charcter) is True  :

            if charcter in string.ascii_lowercase:

                if charcter in secret_word:
                    indexx=[i for i, value in enumerate(secret_word) if value == charcter]
                    for ee in indexx:
                        get_guesse_list[ee]=charcter

                    S=listToString(get_guesse_list)
                    print('Good guess :',S)

                else:
                    guesses = guesses - 1
                    if charcter in Vowels:
                        guesses = guesses - 1

                    print('Oops! that letter is not in my word. Please guess another letter :', S ) 
            else:

                if warnings != 0:
                    warnings -=1
                    print("Oops! You've already guessed that letter. You Have",warnings ,"Warnings left:" , S)
                elif guesses > 0 and warnings == 0 : 
                    guesses -=1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:" , S)
                    

        elif str.isalpha(charcter) is False :
            
            if warnings != 0 :
                warnings -= 1
                print('Oops! That is not a valid letter. You have', warnings  ,'warnings left:' , S)  
                
            elif guesses > 0 and warnings == 0 : 
                guesses -= 1
                print('You have no warnings left so you lose one guess. You have', guesses  ,'guesses left:' , S)


        letters_guessed.append(charcter) 
        for charcter in letters_guessed:
            if (charcter in string.ascii_lowercase) :
                index = string.ascii_lowercase.index(charcter) 
                string.ascii_lowercase  = string.ascii_lowercase[ :index] +  string.ascii_lowercase[index+1 : ]


        print('--------------') 
        is_word_guesse= all (letters in get_guesse_list  for letters in secret_word)
        
        if is_word_guesse is True: 
            Total_score = guesses*len(set(secret_word))
            print('congratulations, you won!')
            print('Your secrt word is', S)
            print('Your total scoe for this game is :',Total_score)
            break
    if is_word_guesse is False: 
        print('Sorry, you ran out of guesses. The word was else.', secret_word)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    
    MY_WORD = re.sub(r"\s+", "", my_word)
    #print(MY_WORD)
    #print(other_word)
    if len(MY_WORD)!=len(other_word): #length is not consistent 
        return False  

    else: #length is  consistent 
        length=len(MY_WORD)
        for i in range(length): 
    
            if MY_WORD[i]!='_' and MY_WORD[i]!=other_word[i]:
                return False 

            if MY_WORD[i]=='_' :
                j=i+1 
                for j in range(length): 
                    if other_word[i]==other_word[j] and MY_WORD[i]!=MY_WORD[j]: 
                        
                        return False 

        
        return True 

"""
print(match_with_gaps('a_ ple','bannana'))
print(match_with_gaps('a_ _ le','apple'))
print(match_with_gaps('a_ ple','apple'))
"""


def show_possible_matches(my_word):
    other_word=[]
                
    for words in wordlist:
        if match_with_gaps(my_word, words) is True:
            other_word.append(words)
        

    print('You have', len(other_word), 'possible word matches ')
    print('Possible word matches are : \n',other_word)



def hangman_with_hints(secret_word):
    #print(secret_word)
    X = len(secret_word)
    guesses = 6
    warnings = 3 

    get_guesse_list=[]
    for i in range(X):
        get_guesse_list.append("_ ")

    S=listToString(get_guesse_list)

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ', X ,' letters long.')
    print('You have ', warnings ,' warnings left')
    print('------------------------')

    while guesses > 0 :
        print('You have ', guesses ,' guesses left')
        print('Available_letters :  ' ,string.ascii_lowercase)

        charcter = input('Please guess a letter :') 
        if str.islower(charcter) is False :
            charcter=charcter.lower()

        if guesses <= 4 and charcter == '*':
    
            # Remove all the spaces from my_word
            my_word = re.sub(r"\s+", "", S )
            #print('My word with out space is:', my_word)

            show_possible_matches(my_word)


        elif str.isalpha(charcter) is True and str.islower(charcter) is True  :

            if charcter in string.ascii_lowercase:

                if charcter in secret_word:
                    indexx=[i for i, value in enumerate(secret_word) if value == charcter]
                    for ee in indexx:
                        get_guesse_list[ee]=charcter

                    S=listToString(get_guesse_list)
                    print('Good guess :',S)

                else:
                    guesses = guesses - 1
                    if charcter in Vowels:
                        guesses = guesses - 1

                    print('Oops! that letter is not in my word. Please guess another letter :', S ) 
            else:

                if warnings != 0:
                    warnings -=1
                    print("Oops! You've already guessed that letter. You Have",warnings ,"Warnings left:" , S)
                elif guesses > 0 and warnings == 0 : 
                    guesses -=1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:" , S)
                    

        elif str.isalpha(charcter) is False :
            #or str.islower(charcter) is False :

            if warnings != 0 :
                warnings -= 1
                print('Oops! That is not a valid letter. You have', warnings  ,'warnings left:' , S)  
                
            elif guesses > 0 and warnings == 0 : 
                guesses -= 1
                print('You have no warnings left so you lose one guess. You have', guesses  ,'guesses left:' , S)


        letters_guessed.append(charcter) 
        for charcter in letters_guessed:
            if (charcter in string.ascii_lowercase) :
                index = string.ascii_lowercase.index(charcter) 
                string.ascii_lowercase  = string.ascii_lowercase[ :index] +  string.ascii_lowercase[index+1 : ]


        print('--------------') 
        
        is_word_guesse= all (letters in get_guesse_list  for letters in secret_word)
        
        if is_word_guesse is True: 
            Total_score = guesses*len(set(secret_word))
            print('congratulations, you won!')
            print('Your secrt word is', S)
            print('Your total scoe for this game is :',Total_score)
            break
    if is_word_guesse is False: 
        print('Sorry, you ran out of guesses. The word was else.',secret_word)
        



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

    #######################
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    print(secret_word)
    hangman_with_hints(secret_word)
