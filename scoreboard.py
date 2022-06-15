from turtle import Turtle


class Scoreboard(Turtle):
    """the class creates scoreboard at the top of the screen using Turtle object"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """the module writes player's score defined as l_score and r_score attributes"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """the module increases right player's score by one and updates scoreboard"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """the module increases left player's score by one and updates scoreboard"""
        self.r_score += 1
        self.update_scoreboard()
