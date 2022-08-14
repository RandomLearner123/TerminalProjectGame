# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import random
choices = ["rock", "paper", "scissors"]

#player inputs and greetings
print("Hello and welcome to rock, paper, scissors!")
print("you will play rock paper scissors with against a bot and test your luck!")
print("input finish when don't want to play anymore!")
player_choice = input("Player choose one(rock,paper,scissors!):")
print("Player has chosen",  player_choice,  "let's see what bot has chosen!")


#computer's line of code
computer_choice = random.choice(choices)
print(computer_choice)

if player_choice == computer_choice:
    print("it's a tie game!")
elif player_choice == "rock":
    if computer_choice == "paper":
        print("you lost!")
    if computer_choice== "scissors":
        print("you won!")
elif player_choice == "scissors":
    if computer_choice == "rock":
        print("you lost!")
    if computer_choice == "paper":
        print("you won!")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("you won!")
    if computer_choice == "scissors":
        print("you lost!")
elif player_choice == "finish":
    print("thanks for playing my game, have a great day!")