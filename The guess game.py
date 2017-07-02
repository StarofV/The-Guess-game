from random import randint
import os
os.system('color 9')
print(r''' __      __       .__                                  __             __  .__                                                 .__                                                
#   __      __       .__                               
#  /  \    /  \ ____ |  |   ____  ____   _____   ____  
#  \   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
#   \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
#    \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
#         \/       \/          \/            \/     \/
I'd recommend running this in cmd :D 
This was made by Dogeman ~DogeSec~ and by Opicaak, add me in discord :D Dogeman ~DogeSec~#5068''')


def another(x):
    guessit = randint(1, x)
    guess = None
        
    print("Enter your guess between 1 and %d\n" % x)
    
    while guess != guessit:
        try:
            
            guess = int(input())
            
            if guess > guessit:
                print("Lower...")
                
            else:
                print("Higher...")
                
        except ValueError:
            print("Please enter a number! Letters can't be entered")
 
        if  guess == guessit:
            print('You got it, the answer was', guessit)
            y = x + 10
            move_on(y)
        
            
def move_on(y):
    print("Welcome to the next level, keep in mind each level gets harder!\n")
    another(y)

if __name__ == '__main__':
    
    try:
        another(10)
    except KeyboardInterrupt:
        print("Closing program.")
    except:
        print("There was an error while trying to run the program!")
