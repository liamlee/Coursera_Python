# implementation of card game - Memory
# 2013-05-24

import simplegui
import random

#global values
pos_list = []
card_list = []
exposed = []
num_list = range(0,8) + range(0,8)
unmatch_num = 0
unmatch_list = []
Moves = 0

# helper function to initialize globals
def set_list():
    global pos_list,card_list,exposed
    i = 0
    pos_start = 12.5
    step = 50
    while i < 16:
        #set the position of each numner
        pos_list.append([pos_start+i*step,65])
        #set the position of each card
        card_list.append([(0+i*step,100),(0+i*step,0),(50+i*step,0),(50+i*step,100)])
        #
        exposed.append(False)
        i+=1
        
def init():
    global mun_list,pos_list,card_list,exposed,Moves
    random.shuffle(num_list)
    Moves = 0
    label.set_text("Moves = " + str(Moves))
    i = 0
    while i < 16:
        exposed[i] = False
        i+=1

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed,unmatch_num,unmatach_list,num_list,Moves
    temp = pos[0] - 50
    index = 0
    while int(temp) > 0:
        index += 1
        temp -= 50
    if ~exposed[index]:
        #no unmatch card before,set the current to be the first unmatch card.
        if unmatch_num == 0:
            exposed[index] = True
            unmatch_list.append(index)
            unmatch_num += 1
            Moves += 1
        #
        elif unmatch_num == 1:
            if num_list[unmatch_list[0]] == num_list[index]:
                exposed[index] = True
                unmatch_list.pop()
                unmatch_num = 0
            else:
                exposed[index] = True
                unmatch_list.append(index)
                unmatch_num += 1
        #no more than two unmatched card should be display
        else:
            exposed[index] = True
            exposed[unmatch_list.pop()] = False
            exposed[unmatch_list.pop()] = False
            unmatch_list.append(index)
            unmatch_num = 1     
            Moves += 1
    label.set_text("Moves = " + str(Moves))
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    i = 0
    for em in num_list:
        if exposed[i]:
            canvas.draw_text(str(em),pos_list[i],50,"white")
        else:
            canvas.draw_polygon(card_list[i],1,"black","green")
        i+=1 


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
set_list()
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric