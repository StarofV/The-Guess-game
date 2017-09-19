from random import randint
from time import sleep
from os import name as os_name
from os import system as os_system


def clear_screen():
    os_system("cls" if os_name == "nt" else "clear") 

def another(x):
    guessit = randint(1, x)
    guess = 0
        
    print("Enter your guess between 1 and %d" % x+1)
    
    while guess != guessit:
        try:
            guess = int(input("Number # ")))
            print("Lower" if guess < guessit else "Higher")                
        except ValueError:
            print("Please enter a number! Letters can't be entered")
    print('You got it, the answer was', guessit)
    move_on(x + 10)
        
            
def move_on(y):
    print("Welcome to the next level, keep in mind each level gets harder!")
    another(y)

if __name__ == '__main__':
    clear_screen()
    
    print(r''' __      __       .__                                  __             __  .__                                                 .__                                                
#   __      __       .__                               
#  /  \    /  \ ____ |  |   ____  ____   _____   ____  
#  \   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
#   \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
#    \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
#         \/       \/          \/            \/     \/
I'd recommend running this in cmd :D 
This was made by SpaceDoge ~DogeSec~ and by Opicaak, add me in discord :D SpaceDoge ~DogeSec~#5068.
Also Special thanks to Opicaak, this wouldn't be possible without him! <3 ''')
    
    try:
        another(10)
    except KeyboardInterrupt:
        print("Closing program.")
        sleep(1)
        clear_screen()
