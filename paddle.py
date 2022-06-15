from turtle import Turtle


class Paddle(Turtle):
    """this class creates Paddle object out of Turtle object"""

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """the module takes Paddle object's position on y axis and increases it by 20px"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """the module takes Paddle object's position on y axis and decreases it by 20px"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


def middle_line(center=(0, 300)):
    """the function creates line on the screen using Turtle object and pendown() method"""
    line = Turtle()
    line.hideturtle()
    line.color("yellow")
    line.penup()
    line.goto(center)
    line.setheading(180)
    while line.ycor() > -300:
        line.pendown()
        line.goto(0, line.ycor() - 30)
        line.penup()
        line.goto(0, line.ycor() - 30)
