#http://www.codeskulptor.org/#user31_2GTNZ3Tb2V_1.py
# Examples of mouse input
# implementation of card game - Memory

import simplegui
import random

temp1=[]
turn_count = 0
card_pos = [[0, 0], [50, 0],[50, 100],[0, 100]]
number_pos = [8, 75]
number_expose = []

# helper function to initialize globals
def new_game():
    global temp1,turn_count
    temp1 = range(8)
    temp1.extend(range(8))
    random.shuffle(temp1)
    turn_count = 0
    print temp1
    print turn_count
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    seq = pos // 50
    
    pass
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    global temp1,card_pos, number_pos, number_expose
    card_pos = [[0, 0], [50, 0],[50, 100],[0, 100]]
    number_pos = [8, 75]
    for num in temp1:
        canvas.draw_polygon(card_pos, 3, 'Yellow', 'Green')
        card_pos[0][0] += 50
        card_pos[1][0] += 50
        card_pos[2][0] += 50
        card_pos[3][0] += 50
        
    for num in temp1:
        canvas.draw_text(str(num), number_pos, 70, 'White')
        number_pos[0] += 50

    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = ") 
label = frame.add_label(str(turn_count))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
