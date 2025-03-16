# rock , paper sicer
import random

def play():
  user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
  computer = random.choice(['r', 'p', 's'])

  #   khurram   computer
  if user == computer:
    return 'It\'s a tie'
    

  if is_win(user, computer):
    return 'You won!' # Indented to be part of the 'if' block

  return 'You lost! computer choice',(computer), # Indented at the same level as the 'if' block

def is_win(player, opponent):
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
    return True

print(play()) # Moved outside the function definitions

