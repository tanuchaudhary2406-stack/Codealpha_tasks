import random
# random module to select a random word

# List of possible words
words = ["lotus", "rose", "green", "white", "apple"]

# Randomly choose a word from the list
word = random.choice(words)

# Create a display list with underscores for each letter in the word 
display = ["_"] * len(word)

# Total wrong attempts allowed
attempts = 6

# List to store letters that have been gusssed
guessed_letter = []

# Welcome message
print("Welcome to hangmna game")
print("Guess the word leter by letter")

# Main game loop: continue until attempts are left and word not completely guessed
while attempts > 0 and "_" in display:
    # Show the current state of the word
    print("\nWord:"," ".join(display))
    # Show letters that have already been guessed
    print("Guessed letters :", ",".join(guessed_letter))

    # Take input from user, convert to lowerase and remove extra space
    guess = input("Enter a letter:").lower().strip()
    
    # Input validation: must be a single alphabet letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter (a-z).")
        continue  # ask for input again

    # Check if the letter was already guessed
    if guess in guessed_letter:
        print("you already guessed that letter!")
        continue  # ask for input again 

    # Add the guessed letter to the guessed_letter list
    guessed_letter.append(guess)

    #If the guessed letter is in the word
    if guess in word:
        print("correct guess!")
        # replace underscores in display with the gussed letter
        for i, letter in enumerate(word):
            if letter == guess:
                display[i] = guess
    else:
        # Wrong guess, reduce attepmts
        attempts -= 1
        print("wrong guess! Attempts left: {attempts}")

# After loop ends, check if word is completely guessed
if "_" not in display:
    print("\n Congratulations! you guessed the word:", word)
else:
    print("\n Game over! The word was:", word)