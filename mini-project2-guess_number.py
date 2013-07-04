# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# @Author liamlee
# @2013-05-05
import simplegui
import random
import math

# initialize global variables used in your code
rang_num = 100
# Number of chance
count = 7



# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global rang_num
    global count 
    count = 7
    rang_num = random.randrange(0,100)
    
    print 'New game,Range is from 0 to 100'
    print 'Number of remaining guesses is ',count
    print ''
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global rang_num
    global count 
    count = 10 
    rang_num = random.randrange(0,1000)
    
    print 'New game,Range is from 0 to 1000'
    print 'Number of remaining guesses is ',count
    print ''

def init():
    range100()
    
def get_input(guess):
    # main game logic goes here	
    global rang_num
    global count
    
    count = count -1
    if count < 0:
        print 'Sorry man,you run out of all the chance!\nGood luck for next time!\n'
        init()
        
    guess_num = int(guess)
    print 'Guess was ',guess_num
    print 'Number of remainig guesses is ',count
    
    if rang_num > guess_num:
        print 'Higher! \n'
    elif rang_num < guess_num:
        print 'Lower! \n'
    else:
        print 'Correct! \n'
        init()
    
# create frame
f = simplegui.create_frame("Guess_number",200,200)

# register event handlers for control elements
f.add_button("Range is [0,100)",range100,200)
f.add_button("Range is [0,1000)",range1000,200)
f.add_input("Enter your guess",get_input,200)


# start frame
init()

# always remember to check your completed program against the grading rubric
