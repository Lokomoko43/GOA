from turtle import *
# start of homework
# main settings
speed(10)
width(7)


def door(distance, angle, x, y, color_name):
    color(color_name)
    forward(distance)
    right(angle)
    forward(x)
    right(angle)
    forward(y)


def roof(color_name, distance):
    color(color_name)
    begin_fill()
    right(150)
    forward(distance)
    left(120)
    forward(distance)
    end_fill()


def square(distance, color_name):
    color(color_name)
    for i in range(4):
        forward(distance)
        left(90)
# end of main settings


# step 1: make a square
square(200, "purple")
# end of step 1

# step 2: make a door
forward(70)
left(90)
door(100, 90, 60, 100, "yellow")
# end of step 2

# step 3: make a roof
penup()
goto(200, 200)
pendown()
roof("red", 200)
# end of step 3

# final step 1: window 1
penup()
goto(75, 120)
pendown()
right(150)
square(60, "cyan")
#end of final step 1

#final step 2: windown 2
penup()
goto(185, 120)
pendown()
square(60, "cyan")
#end final step 2
exitonclick()
#end pf homework
