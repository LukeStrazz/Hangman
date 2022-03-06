word = "Secret"
allowed_errors = 7
guesses = []
done = False
# Functions
def printboard():
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end="")
        else:
            print("_", end="")
    print("")

def checkTheword():
    for letter in word:
        if letter.lower() not in guesses:
            return False
    return True





while not done:
    guess = input(f"Allowed Errors left{allowed_errors},Next Guess:")
    guesses.append(guess.lower())

    printboard()
    if (guess.lower() not in word.lower()):
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done=True
    done =checkTheword()

if done:
    print(f"You found the word! It was {word}")
else:
    print(f"You lost the word was {word}")
