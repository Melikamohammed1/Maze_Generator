import turtle
import random
import time

# ---------------- SCREEN ---------------- #
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Generator")
wn.setup(1300, 700)
wn.tracer(0)

# ---------------- DRAWING TURTLE ---------------- #
wall_t = turtle.Turtle()
wall_t.hideturtle()
wall_t.speed(0)
wall_t.color("white")
wall_t.penup()

turtle.done()
# ---------------- CONFIG ---------------- #
ROWS = 20
COLS = 25
CELL_SIZE = 24

# ---------------- DATA ---------------- #
northWall = [[1] * COLS for _ in range(ROWS)]
eastWall = [[1] * COLS for _ in range(ROWS)]
visited = [[False] * COLS for _ in range(ROWS)]
# ---------------- HELPERS ---------------- #
def cell_to_screen(r, c):
    x = -600 + c * CELL_SIZE
    y = 300 - r * CELL_SIZE
    return x, y


def draw_line(x1, y1, x2, y2):
    wall_t.goto(x1, y1)
    wall_t.pendown()
    wall_t.goto(x2, y2)
    wall_t.penup()


# ---------------- DRAW MAZE ---------------- #
def draw_maze():

    wall_t.clear()

    for r in range(ROWS):
        for c in range(COLS):

            x, y = cell_to_screen(r, c)

            # North wall
            if northWall[r][c] == 1:
                draw_line(x, y, x + CELL_SIZE, y)

            # East wall
            if eastWall[r][c] == 1:
                draw_line(
                    x + CELL_SIZE,
                    y,
                    x + CELL_SIZE,
                    y - CELL_SIZE
                )

    # Bottom border
    for c in range(COLS):

        x, y = cell_to_screen(ROWS - 1, c)

        draw_line(
            x,
            y - CELL_SIZE,
            x + CELL_SIZE,
            y - CELL_SIZE
        )

    # Left border
    for r in range(ROWS):

        x, y = cell_to_screen(r, 0)

        draw_line(
            x,
            y,
            x,
            y - CELL_SIZE
        )