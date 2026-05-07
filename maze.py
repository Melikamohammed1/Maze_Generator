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