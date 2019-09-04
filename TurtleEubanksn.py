import turtle

wn = turtle.Screen()
wn.title("smallboi's small journey")
wn.bgcolor("blue")
smallboi = turtle.Turtle()
smallboi.shape("turtle")
smallboi.color("black")
#everything to set up turtle and bg
###################################
smallboi.pensize(10)
smallboi.forward(50)
smallboi.right(90)
smallboi.forward(50)
smallboi.left(180)
smallboi.forward(100)
smallboi.right(180)
smallboi.forward(50)
smallboi.right(90)
smallboi.forward(50)
smallboi.left(90)
smallboi.forward(50)
smallboi.left(180)
smallboi.forward(100)
#First letter
##########################
smallboi.penup()        #adjust position w/o writing
smallboi.right(90)
smallboi.forward(100)
smallboi.pendown()     #resume writting
smallboi.right(90)
smallboi.forward(100)
#finished second letter
#############################
wn.exitonclick()