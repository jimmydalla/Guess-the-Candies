import random
from colorama import Fore,Back,Style

name = input(Fore.BLUE+"What is your name? :")
print(Fore.GREEN)
print(f" Hi {name} Guess how many candies are there in the jar...")

count = 1
No_of_candies = random.randint(40,60)
while count<=5:
  guess = int(input("Enter the guess :"))
  count = count+1
  
  if guess<No_of_candies:
    print("A little higher")
  elif guess>No_of_candies:
    print("A little lower")
  else:
    print("You have won the game")
  if count>5:
    print("You've run out of chances")


  
  

