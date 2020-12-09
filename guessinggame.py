secret_word = input("Enter a Secret Word!")
guess = ""
guessed_count = 0
guess_limit = 20
out_of_guesses = False
while guess != secret_word and not (out_of_guesses):
    if guessed_count < guess_limit:
        guess = input("Enter guess: ")
        guessed_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
     print("Out of Guesses, the game is lost.")
else:
     print("You win!")
