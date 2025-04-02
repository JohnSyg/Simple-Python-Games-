import random
from collections import Counter

names_of_fruits = "apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon"
names_of_fruits = names_of_fruits.split(" ")
chosen_word = random.choice(names_of_fruits)

if __name__ == '__main__':
    print("Guess the word! Hint: Its a fruit")

    for i in chosen_word:
        print("_", end=" ")
    print()

    playing = True
    letterGuessed = ""
    chances = len(chosen_word) + 2
    correct = 0
    flag = 0

    try:
        while (chances != 0) and flag ==0:
            print()
            chances -= 1

            try:
                guess = str(input("Enter a letter to guess : "))
            except:
                print("Enter only a letter !")
                continue

            if not guess.isalpha():
                print("Enter only a LETTER")
                continue
            elif len(guess) > 1:
                print("Enter only a SINGLE letter")
                continue
            elif guess in letterGuessed:
                print("You hae already guessed that letter")
                continue
            if guess in chosen_word:
                k = chosen_word.count(guess)
                for _ in range(k): letterGuessed +=guess
            for char in chosen_word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(chosen_word)):
                    print(char,end=' ')
                elif (Counter(letterGuessed) == Counter(chosen_word)):
                    print("The word is: ", end=' ')
                    print(chosen_word)
                    flag = 1
                    print("Congratulations , You won!")
                    break 
                    break
                else:
                    print('_', end=' ')
        if chances <= 0 and (Counter(letterGuessed) != Counter(chosen_word)):
            print()
            print("You lost ! Try again.")
            print("The word was {}".format(chosen_word))
    except KeyboardInterrupt:
        print()
        print("Bye! Try again.")
        exit()
