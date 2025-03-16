# import random 
# print ("Welcome to pasword Genrator ")


# chars='asdfghjklqwertyuiozxcvbnm,,./!@#$%^&*'


# num= int (input ("amount of  Pasword that to be genrate :"))
# length =int(input ("input you paswd length"))
# print ('\nhear are your pasword:')
# for pwd in range (num):
#     password=""
#     for c in range(length):
#         password += random.choice(chars)
#         print(password)
        
        
        
        
        
        
import random 
print("Welcome to Password Generator 🔐")

# Available characters for password
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

# Taking user input
num = int(input("Amount of Passwords to generate: "))
length = int(input("Input your Password length: "))

print("\nHere are your passwords:")

# Loop to generate multiple passwords
for pwd in range(num):
    password = ""
    for c in range(length):
        password += random.choice(chars)  # Add random character from chars
    print(password)  # Print full password once

        
        