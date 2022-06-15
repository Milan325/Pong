from turtle import Turtle


class Ball(Turtle):
    """this class creates ball out of Turtle object"""

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.1

    def move(self):
        """the module takes coordinates of ball and increases it by one, moving Ball object across the screen"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """the module changes the direction of Ball on y axis after hitting the paddle"""
        self.y_move *= -1

    def bounce_x(self):
        """the module changes the direction of Ball on x axis after hitting top and bottom screen walls"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """the module returns Ball object to the center of the screen and adds 10% to the ball speed"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()







