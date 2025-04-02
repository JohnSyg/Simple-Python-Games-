import random

name = input("What is your name ?? : ")
print("Good luck ! " + name)

words = ["rainbow" , "computer" , "science" , "programming" , "python" , "mathematicts" , "player" , "condition" , "reverse" , "water" , "board" , "geeks"]

chosen_word = random.choice(words)

print("Please provide letters in order to create the correst word")

guesses = ""

turns = 12

while turns > 0:
    failed = 0

    for char in chosen_word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You win !! The word is " + chosen_word)
        break

    print()
    guess = input("Enter a character : ")

    guesses += guess

    if guess not in chosen_word:
        turns -= 1
        print("Wrong !! You have " + str(turns) + " more turns")

        if turns == 0:
            print("You have run out of tries , you lose !!")