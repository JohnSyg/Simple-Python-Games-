import random

print("Welcome to a game of guessing a number. You have 7 chances")

Number_To_Guess = random.randrange(100)
print ("Hint!! The number is : ", Number_To_Guess)

Chances = 7

Guess_Counter = 0

while Guess_Counter < Chances:
    Guess_Counter += 1
    My_Guess = int(input("Please enter the number you think the answer is : "))

    if Guess_Counter >= Chances and My_Guess != Number_To_Guess:
        print ("Sorry you run out of tries the number was : ", Number_To_Guess)
        break

    elif My_Guess < Number_To_Guess:
        print ("The number you guessed is lower than the correct one, please try again.")

    elif My_Guess > Number_To_Guess:
        print ("The number you guessed is higher than the correct one, please try again.")

    elif My_Guess == Number_To_Guess:
        print (f"Congrats you have found the number {Number_To_Guess} in your {Guess_Counter} attempt")
        break

