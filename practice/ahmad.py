import random
while True:


    user = int(input("Enter a Number Between 1 - 10 "))
    if  not  1 <= user <= 10:
      print("Enter Your Number Between 1 and 10")
      continue
    computer = random.randint(1,10)

    if user == computer:
        print(f"You Win,Computer Input was {computer}")
    else:
        print(f"You Lose, Computer Input was {computer}")