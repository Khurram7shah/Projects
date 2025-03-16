# import random
# from words import words
# from main_stage import main_stage
# word_guess = random.choice(words)
# attempts=6
# dashes=['_']*len(word_guess)
# word_guessed=''
# guessed=False

# def find(word,ltr):
#     index_list=[]
#     for i, j in enumerate(word):
#         if i==ltr:
#             index_list.append(i)
#     return index_list 
# print ('lets play game ')       

# while attempts>0 and not guessed:
#     letter=input('guess a letter:')
#     if letter in word_guessed:
#         print ('already guess, try another :,')
#         print (' '.join(dashes))
#     elif letter in word_guess:
#         indices= find(word_guess,letter )
#         for index in indices:
#             dashes=[index]=letter
#             word_guessed=''.join(dashes)
#             print (' '.join(dashes))
#     elif letter not in word_guess:
#         attempts-=1
#         print(main_stage(attempts))
#         print('letter not found in word  \n only {} attemts left'.format(attempts))
        
#     else:
#         print ('invalid input ')      
              
#     if word_guessed ==word_guess:
#         guessed=True
        
# if guessed:
#     print("you win")    
    
# else:
#     print ("you lost ") 
#     print (f"guess word is {word_guess}")       
               
        
        
