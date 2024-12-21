from turtle import RawTurtle

class ShapeDrawer():
    def __init__(self, raw_tutrle: RawTurtle):
        self.raw_turtle = raw_tutrle

    def heart(self, colour: str = "red") -> None:
        self.raw_turtle.clear()
        self.raw_turtle.reset()
        self.raw_turtle.speed(1)
        self.raw_turtle.penup()
        self.raw_turtle.goto(0, -200)
        self.raw_turtle.pendown()
        self.raw_turtle.color(colour)
        self.raw_turtle.begin_fill()
        self.raw_turtle.left(140)
        self.raw_turtle.forward(224)
        for _ in range(200):
            self.raw_turtle.right(1)
            self.raw_turtle.forward(2)
        self.raw_turtle.left(120)
        for _ in range(200):
            self.raw_turtle.right(1)
            self.raw_turtle.forward(2)
        self.raw_turtle.forward(224)
        self.raw_turtle.end_fill()
        self.raw_turtle.hideturtle()

    def square(self, colour: str = "blue") -> None:
        self.raw_turtle.clear()
        self.raw_turtle.reset()
        self.raw_turtle.speed(1)
        self.raw_turtle.penup()
        self.raw_turtle.goto(-50, -50)
        self.raw_turtle.pendown()
        self.raw_turtle.color(colour)
        self.raw_turtle.begin_fill()
        for _ in range(4):
            self.raw_turtle.forward(100)
            self.raw_turtle.right(90)
        self.raw_turtle.end_fill()
        self.raw_turtle.hideturtle()

    def star(self, colour: str = "gold") -> None:
        self.raw_turtle.clear()
        self.raw_turtle.reset()
        self.raw_turtle.speed(1)
        self.raw_turtle.penup()
        self.raw_turtle.goto(-50, 50)
        self.raw_turtle.pendown()
        self.raw_turtle.color(colour)
        self.raw_turtle.begin_fill()
        for _ in range(5):
            self.raw_turtle.forward(150)
            self.raw_turtle.right(144)
        self.raw_turtle.end_fill()
        self.raw_turtle.hideturtle()

    def circle(self, colour: str = "green") -> None:
        self.raw_turtle.clear()
        self.raw_turtle.reset()
        self.raw_turtle.speed(1)
        self.raw_turtle.penup()
        self.raw_turtle.goto(0, -75)
        self.raw_turtle.pendown()
        self.raw_turtle.color(colour)
        self.raw_turtle.begin_fill()
        self.raw_turtle.circle(75)
        self.raw_turtle.end_fill()
        self.raw_turtle.hideturtle()

    def clear_screen(self):
        self.raw_turtle.clear()
        self.raw_turtle.reset()
