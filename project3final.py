
"""
Eric Gomez
Project #3
Guessing game where player has five chances to guess random number
"""
import random

#The funtion main calls and runs the whole program by getting the different inputs and outputs of the other funtions
def main():
    money, start_money = getInput()
    money = Game(money)
    getOutput(money, start_money)

#The function getInput gets the input from the user of how much money that they have and returns it
def getInput():
    print("Welcome to this very fair game!")
    money = int(input("How much money do you have? "))
    start_money = money
    return money, start_money
#The funtion Game(money) generates a random number between 1 and 50 and then runs the playerChoice funtion to run the game and see if the player guesses right. It also verifies that the player has enough money to play with and that they want to continue to play. 
def Game(money):
    answer = 'y'
    while answer == 'y'  and money > 0:
        money -= 1
        #generates random number for guessing game
        computer = random.randint(1,50)
        money = playerChoice(money, computer)
        print("Your money = $", money)
        answer = input("Would you like to play again? ").lower()
        while answer != 'y' and answer != 'n':
            answer = input("Incorrect input. Would you like to play again? (y/n)").lower()
    return money

#playerChoice checks if the user guessed the random number that the function Game(money) produced and runs until they get it or when they guessed 5 times, whichever comes first
def playerChoice(money, computer):
    
    for i in range(5):
        print("Guess a number between 1 and 50")
        choice = int(input("Make your choice: "))
        while choice < 0 or choice > 50:
                choice = int(input("Incorrect input. Make your choice: "))
            #if-statements for win condition or displays whether too high or too low
        if choice == computer:
             print("You win!")
             money += 3
             break
        elif choice > computer:
            print("Too high")
        else:
            print("Too low")
    return money

#getOutput gives you the result of the game of how much you won, lost, or if you broke even
def getOutput(money, start_money):
    if money> start_money:
        print("You have won $", money - start_money)
    elif money == start_money:
        print("You broke even.")
    elif money == 0:
        print("You are broke.")
    else:
        print("You lost $", start_money - money)
    print("Game is over")

main()