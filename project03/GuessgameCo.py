  
import random

def computer_guess(x):
    low = 1 # low number 
    high = x 
    feedback = '' 
   
    
    
    # fedback='c'
            #c
    while feedback != 'c':# true
        
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Only one number left

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay! The computer guessed your number {guess} correctly.") 
    #c

# Example usage:
computer_guess(100) 


# You can replace 100 with any upper limit

    
    
    
    
    
    
    
    
