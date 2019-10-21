from turtle import *


DEFAULT_DISTANCE = 75
START_X = -100


# draws a single square
def draw_square(side_len=50):
    # set the colors and start the fill
    color('black', '#5c67ff')
    begin_fill()

    # set the pen down and start drawing
    pendown()
    for i in range(4):
        forward(side_len)
        left(90)
    penup()

    # fill the shape
    end_fill()


# draws multiple squares
def draw_squares(num_rows=3, num_cols=3):
    penup()
    current_y = -75

    # loop through each row we want to draw
    for row in range(num_rows):
        # reset the pen to the left and down
        penup()
        setx(START_X)
        sety(current_y)
        current_y -= 50

        # loop through each cell we want to draw
        for col in range(num_cols):
            # draw a square
            draw_square()

            # move the pen to draw the circle in the square
            forward(25)
            draw_circle()

            # move the pen in preparation to draw another square
            forward(25)


# draws a triangle
def draw_triangle(side_len=50):
    # set the colors and start the fill
    color('#c0c0c0', 'green')
    begin_fill()

    # set the pen down and start drawing
    pendown()
    for i in range(3):
        forward(side_len)
        left(120)
    penup()

    # fill the shape
    end_fill()


# draws a circle
def draw_circle(radius=25):
    # set the colors and start the fill
    color('black', '#ffdd5c')
    begin_fill()

    # set the pen down and start drawing
    pendown()
    circle(radius)
    penup()

    # fill the shape
    end_fill()


def main():
    # set up general turtle defaults
    speed(0)        # this adjusts how fast the pen draws (0-10)
    shape('turtle') # this adjusts the shape of the pen

    # set the starting x-coordinate of the pen
    penup()
    setx(START_X)

    # begin_fill()
    draw_square()

    # move pen over
    forward(DEFAULT_DISTANCE)

    # draw a triangle
    draw_triangle()

    # move pen over
    forward(DEFAULT_DISTANCE)

    # draw a circle
    draw_circle()

    # move pen over
    forward(DEFAULT_DISTANCE)

    # draw a group of squares
    draw_squares(num_rows=4, num_cols=4)

    # done drawing (without this, your GUI window will exit)
    done()


if __name__ == '__main__':
    main()