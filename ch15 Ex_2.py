# %%
import turtle

class Point:
    """ Represents a Point."""

class Rectangle:
    """ Represents a Rectangle.
        attributs: width, height, corner """

class Circle:
    """ Represents a Circle.
        attributs: center, radius"""

def draw_rect(turt, rect):

    turt.showturtle()
    turt.up()
    turt.goto(rect.corner.x, rect.corner.y)
    turt.down()
    turt.forward(rect.width)
    turt.left(90)
    turt.forward(rect.height)
    turt.left(90)
    turt.forward(rect.width)
    turt.left(90)
    turt.forward(rect.height)

def draw_circle(turt, circle):

    turt.showturtle()
    turt.up()
    turt.goto(circle.center.x, circle.center.y)
    turt.down()
    turt.circle(circle.radius)

def main():

    rect = Rectangle()
    rect.width = 100.0
    rect.height = 100.0
    rect.corner = Point()
    rect.corner.x = 0
    rect.corner.y = 0

    circle = Circle()
    circle.radius = 50
    circle.center = Point()
    circle.center.x = 100
    circle.center.y = 100

    turt = turtle.Turtle()
    draw_rect(turt, rect)
    draw_circle(turt, circle)

# %%
if __name__ == "__main__":
    main()

# %%
