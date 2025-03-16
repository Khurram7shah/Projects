import random
from words import words
word_to_guess=random.choice(words)
attempts=7
dashes=["_"]*len(word_to_guess)
word_guessed=''
guessed=False
# ------


def find(word,ltr):
    index_list=[]
    for i, j in enumerate(word):
        if j==ltr:
            index_list.append(i)
    return index_list        



while attempts >0 and not guessed:
    letter= input("Guess a letter:")
    if letter in word_guessed:
        print("already guessed , try another :")
        print (''.join(dashes))
    elif letter in words   :
        indices= find(words,letter)
        for index in indices :
            dashes[index]=letter
             
    elif letter not in words:
        attempts-=1
        print ("Letter not found in word, try again !")
    else :
        print("invaild input")         