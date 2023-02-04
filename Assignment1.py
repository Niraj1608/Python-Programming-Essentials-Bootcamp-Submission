#The program should display one of three messages each time it is run: "Today will be a lucky day", "You will meet someone new and interesting", or "Watch out for obstacles in your path".
#To do this, you can use the random module and the if and elif statements to select one of the messages at random.

import random

def display_message():
    messages = ["Today will be a lucky day", "You will meet someone new and interesting", "Watch out for obstacles in your path"]
    print(random.choice(messages))

if __name__ == '__main__':
    display_message()
