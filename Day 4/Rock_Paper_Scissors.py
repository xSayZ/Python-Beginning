import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


Input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

if Input == "0":
    print("You chose Rock!")
    print(rock)
    r = random.randrange(0, 3)
    if r == 0:
        print("The computer chose Rock:")
        print(rock)
        print("Tie!")
    if r == 1:
        print("The computer chose Paper:")
        print(paper)
        print("You lose!")
    if r == 2:
        print("The computer chose Scissors:")
        print(scissors)
        print("You win!")

elif Input == "1":
    print("You chose Paper!")
    print(paper)
    r = random.randrange(0, 3)
    if r == 0:
        print("The computer chose Rock:")
        print(rock)
        print("You win!")
    if r == 1:
        print("The computer chose Paper:")
        print(paper)
        print("Tie!")
    if r == 2:
        print("The computer chose Scissors:")
        print(scissors)
        print("You lose!")

elif Input == "2":
    print("You chose Scisors!")
    print(scissors)
    r = random.randrange(0, 3)
    if r == 0:
        print("The computer chose Rock:")
        print(rock)
        print("You lose!")
    if r == 1:
        print("The computer chose Paper:")
        print(paper)
        print("You win!")
    if r == 2:
        print("The computer chose Scissors:")
        print(scissors)
        print("Tie!")



