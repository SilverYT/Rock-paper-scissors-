# Rock, Paper, Scissors with Pythons random module! #

# Imports
import random
import time

# Your Choice
player = input('''
      Please type either 1 for Rock. 2 for Paper. Or 3 for Scissors
      ''')

# What You Can Choose From
if player.strip() == "1":
    print("You have chose Rock")
    
if player.strip() == "2":
    print("You have chose Paper")
    
if player.strip() == "3":
    print("You have chose Scissors")
    
# What Python Can Choose From 
options = [
    'Python has chose Rock', 'Python has chose Paper', 'Python has chose Scissors'
]

# Pythons choice
secs = [1, 2, 3, 4, 5]
time.sleep(random.choice(secs))
python = print(random.choice(options))
time.sleep(10)


