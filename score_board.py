from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.left_score_board()
        self.goto(100, 200)
        self.right_score_board()

    def left_score_board(self):
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

    def right_score_board(self):
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))


    def right_point(self):
        self.clear()
        self.r_score += 1
        self.goto(-100, 200)
        self.left_score_board()
        self.goto(100, 200)
        self.right_score_board()

    def left_point(self):
        self.clear()
        self.l_score += 1
        self.goto(-100, 200)
        self.left_score_board()
        self.goto(100, 200)
        self.right_score_board()