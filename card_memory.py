#http://www.codeskulptor.org/#user31_2GTNZ3Tb2V_6.py
# implementation of card game - Memory

import simplegui
import random



turn_count = 0
turn_flag = 0
draw_flag = 0
card_pos = [[0, 0], [50, 0],[50, 100],[0, 100]]
number_pos = [8, 75]

temp1=[]
number_expose = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False] 	#牌的状态
print len(number_expose)
number_value_expose =[]		#被翻开的同号牌的大小
#print "WTF!",len(number_expose)

expose_tmp = [-1, -1]
pos_tmp =[-1,-1]
seq = [-1,-1]

# helper function to initialize globals
def new_game():
    global temp1,turn_count, number_expose
    temp1 = range(8)
    temp1.extend(range(8))
    random.shuffle(temp1)
    turn_count = 0
    label.set_text("Turns = " + str (turn_count))
    number_expose = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    print number_expose
    print temp1
    print turn_count
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global turn_count, expose_tmp, pos_tmp, seq, number_expose,draw_flag,turn_flag
    count2 = 0 
    mouse = pos[0] // 50
    if turn_flag == 0:
        turn_flag = 1

    if turn_flag == 1:
         

        if	number_expose[mouse] == True:			#牌如果是打开的，忽略此次点击
            turn_flag = 1
        elif  (number_expose[mouse] != True) and (expose_tmp[0] != expose_tmp[1]):
            number_expose[seq[0]]	= False			#将number_expose对应的标记置为假（将牌翻回）
            number_expose[seq[1]]	= False   
                
        seq[0] = pos[0] // 50
        
        if number_expose[seq[0]] == True:			#牌是翻开的，忽略这次点击
            turn_flag = 1
        
        else:
            #print "the postionof the first card ",seq[0]
            expose_tmp[0] = temp1[seq[0]]					#判断是第一张牌是哪一张,存入比较数组
            #print "the first card is ",expose_tmp[0]
            number_expose[seq[0]]	= True					#置牌的状态为翻开
            turn_flag = 2			   						#计数器计第一次
            #print  "the number_expose is ",number_expose
    elif turn_flag == 2:
        seq[1] = pos[0] // 50							#记录第二张牌的序号
        #print "the seq is ",seq
        expose_tmp[1] = temp1[seq[1]]					#判断是第二张牌是哪一张,存入比较数组
        
        if (number_expose[seq[1]] == True) and (seq[0] == seq[1]) :	#1.牌是翻开的且是同一张牌
            number_expose[seq[1]]	= False				#置牌的状态为翻回
            turn_flag = 1 								#重新开始一轮
            turn_count += 1
            label.set_text("Turns = " + str (turn_count))
            
        elif (number_expose[seq[1]] == True) and (seq[0] != seq[1]) :	#1.牌是翻开的且不是同一张牌
            turn_flag = 2												#忽略此次点击，重新开始第二轮

        elif (seq[0] != seq[1]) and ((number_expose[seq[1]] != True)):	#3牌不是翻开的，不是同一张牌
            if expose_tmp[0] == expose_tmp[1]:			#3.1牌值相等
               # print "the seq is empty? ", seq
                #number_expose[seq[0]]	= True			#将number_expose对应的标记置为真
                number_expose[seq[1]]	= True

                turn_flag = 1							#进入新一轮
                turn_count += 1
                label.set_text("Turns = " + str (turn_count))
            if expose_tmp[0] != expose_tmp[1]:			#3.2两张牌不同值
                number_expose[seq[1]]	= True
                #delay(3)
                #i=10000
                #while(0< i <=10000):						#延时显示
                #    i -= 1
                turn_flag = 1							#重新开始新轮
                turn_count += 1
                label.set_text("Turns = " + str (turn_count))
                
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    global temp1,card_pos, number_pos, number_expose, turn_count,round_flag
    card_pos = [[0, 0], [50, 0],[50, 100],[0, 100]]
    number_pos = [8, 75]
    count1 = 0
    
    if turn_flag == 0:				#初始化
        for num in temp1:										
            canvas.draw_polygon(card_pos, 3, 'Yellow', 'Green')	#先画所有的牌
            card_pos[0][0] += 50
            card_pos[1][0] += 50
            card_pos[2][0] += 50
            card_pos[3][0] += 50
        card_pos = [[0, 0], [50, 0],[50, 100],[0, 100]]			#重置画牌的初始位置
        
    for num in number_expose:
        count1 += 1 
        if (num):
            number_pos[0] = number_pos[0] + (count1-1) *50				#画翻开的数字
            canvas.draw_text(str(temp1[count1-1]), number_pos, 70, 'White')
            #print "num = ",count1
            #print "number expose :",number_expose
            
            number_pos = [8, 75] 
        else:														#画没翻开的牌
            card_pos = [[0, 0], [50, 0],[50, 100],[0, 100]]			#重置画牌的初始位置
            card_pos[0][0] += 50 * (count1-1)
            card_pos[1][0] += 50 * (count1-1)
            card_pos[2][0] += 50 * (count1-1)
            card_pos[3][0] += 50 * (count1-1)            
            canvas.draw_polygon(card_pos, 3, 'Yellow', 'Green')	#画没翻开的的牌
       
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = "+str(turn_count)) 


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
