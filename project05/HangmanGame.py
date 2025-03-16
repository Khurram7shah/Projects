import random
from words import words
from main_stage import main_stage

# Randomly select a word
word_guess = random.choice(words)
attempts = 6
dashes = ["_"] * len(word_guess)  # Create a blank representation of the word
guessed = False
word_guessed = ""

def find(word, ltr):
    """Find all positions of a letter in the word."""
    return [i for i, j in enumerate(word) if j == ltr]

print("🎉 Let's play Hangman! 🎉")
print(" ".join(dashes))  # Show the dashes at the start

while attempts > 0 and not guessed:
    letter = input("\nGuess a letter: ").lower()

    # Validate input
    if not letter.isalpha() or len(letter) != 1:
        print("⚠ Invalid input! Please enter a single letter.")
        continue

    # Check if the letter was already guessed
    if letter in word_guessed:
        print("🔄 Already guessed! Try another letter:")
    elif letter in word_guess:
        # Find and update dashes with the guessed letter
        indices = find(word_guess, letter)
        for index in indices:
            dashes[index] = letter  

        word_guessed = "".join(dashes)  # Convert list to string
        print("✅ Correct! Current progress:")
    else:
        attempts -= 1
        print(main_stage(attempts))  # Show hangman progress
        print(f"❌ Letter not found! Only {attempts} attempts left.")

    print(" ".join(dashes))  # Show updated dashes after each guess

    # Check if the user has guessed the full word
    if "".join(dashes) == word_guess:
        guessed = True

# Final game result
if guessed:
    print("\n🎉 Congratulations! You won! 🎉")
else:
    print(f"\n😞 You lost! The correct word was: {word_guess}")
