from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# defining all the movements of the turtle
def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


# defining what the clear does by clearing the drawing and going back to the home screen penup to not draw path and
# pendown to draw the next sketch
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# getting the screen to listen to keyboard commands
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
