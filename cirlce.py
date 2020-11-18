#your code here
# recommend myturtle.tracer(12,25) for faster animation
import turtle
import random 
import math
import sys 
import altair

sys.setExecutionLimit(60000)


# 3. Throw some darts!
# Inside of a for loop, we'll simulate a random dart, 
# then mark its position in the circle
pi = []

def trials(number_of_darts,trials):
    for trial in range(trials):
        # 1. Make the dartboard
        wn = turtle.Screen()
        # set the world coordinates so that (0,0) is the middle
        # and the board is 2 by 2. 
        wn.setworldcoordinates(-1,-1,1,1)
        # 2. Make the circle. 
        # This circle will have a center of (0,0) and a radius of 1. 
        # we can reuse the code from drawing a circle here! 
        tabs = turtle.Turtle()
        tabs.up()
        tabs.goto(0,-1)
        tabs.down()
        tabs.circle(1)
        tabs.up()
        blue_dots = 0
        
        for i in range(number_of_darts):
            # random.random() generates a random number between 0 and 1
            x = 2*random.random()-1
            # So 2*random.random() generates a random number between 0 and 2
            # We want a random number between -1 and 1
            # so we subtract 1
            # Do the same for the y coordinate
            y = 2*random.random()-1
            tabs.goto(x,y)
            tabs.tracer(1000,1)
            tabs.down()
            radius = math.sqrt(x**2+y**2)

            if radius < 1:
                tabs.dot(2,"blue")
                blue_dots = blue_dots + 1
            else:
                tabs.dot(2,"red")
            tabs.up()
            
        pi.append(((int(blue_dots))/number_of_darts)*4)
# 4. Using the number in circle and total, 
# calculate the percentage that landed in the circle
trials(1000,500)
print(pi)






data = altair.Data(values=pi)
chart = altair.Chart(data)
mark = chart.mark_bar()
X = altair.Axis('values:Q', bin=True)
Y = altair.Axis('count()')
enc = mark.encode(x=X,y=Y)
enc.display()
