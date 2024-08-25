# rules 1: Comparing on the basis of follower count. If user got the person with highest count he scores 1 point and the option selected by him whether A or B for the next turn it becomes A.
# If the winning option is on A and keeps on winning it stays there and option will keep on change.
# rule 2: Game stops when the user get wrong answer. At the end it shows the score.
# rule 3: If the user gets the correct answer, the game continues with the conditions of rule one

from art import logo, vs
from game_data import data
import random
from replit import clear

print(logo)

def get_random_account(data):
  i=random.randint(0,len(data)-1)
  return i


score = 0

win_loose=True


a=get_random_account(data)
print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}")
print(vs)
b=get_random_account(data)
if b==a and a != len(data)-1:
  b += 1
elif b==a and a == len(data)-1:
  b -= 1
print(f"Against B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}")
user_choice = input("Who has more followers? Type 'A' for A or 'B' for B: \n")

while win_loose==True:
   
  if user_choice == 'A' and data[a]['follower_count'] > data[b]['follower_count']:
    score +=1
    b=get_random_account(data)
    clear()
    print(logo)
    print(f"Your score {score}")
   
    print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}")
    print(vs)
    if b==a and a != len(data)-1:
      b += 1
    elif b==a and a == len(data)-1:
      b -= 1
    print(f"Against B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}")
    user_choice = input("Who has more followers? Type 'A' for A or 'B' for B: \n")

  elif user_choice == 'B' and data[a]['follower_count'] < data[b]['follower_count']:
    score +=1
    a=b
    b=get_random_account(data)
    clear()
    print(logo)
    print(f"Your score {score}")
    
    print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}")
    print(vs)
    if b==a and a != len(data)-1:
      b += 1
    elif b==a and a == len(data)-1:
      b -= 1
    print(f"Against B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}")
    user_choice = input("Who has more followers? Type 'A' for A or 'B' for B: \n")

  else:
    print(f"Sorry, your aswer was wrong. Your score final {score}")
    win_loose=False
  
                      


  
  





