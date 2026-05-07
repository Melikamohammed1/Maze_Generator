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
        # ---------------- GENERATOR MOUSE ---------------- #
gen_mouse = turtle.Turtle()
gen_mouse.shape("circle")
gen_mouse.color("orange")
gen_mouse.penup()
gen_mouse.speed(0)
# ---------------- REMOVE WALL ---------------- #
def remove_wall(r, c, nr, nc, direction):

    if direction == "N":
        northWall[r][c] = 0

    elif direction == "S":
        northWall[nr][nc] = 0

    elif direction == "E":
        eastWall[r][c] = 0

    elif direction == "W":
        eastWall[nr][nc] = 0


# ---------------- GENERATE MAZE ---------------- #
def generate_maze():

    stack = []

    r = random.randint(0, ROWS - 1)
    c = random.randint(0, COLS - 1)

    visited[r][c] = True
    stack.append((r, c))

    while stack:

        r, c = stack[-1]

        # Move mouse
        x, y = cell_to_screen(r, c)

        gen_mouse.goto(
            x + CELL_SIZE / 2,
            y - CELL_SIZE / 2
        )

        neighbors = []

        # North
        if r > 0 and not visited[r - 1][c]:
            neighbors.append((r - 1, c, "N"))

        # South
        if r < ROWS - 1 and not visited[r + 1][c]:
            neighbors.append((r + 1, c, "S"))

        # West
        if c > 0 and not visited[r][c - 1]:
            neighbors.append((r, c - 1, "W"))

        # East
        if c < COLS - 1 and not visited[r][c + 1]:
            neighbors.append((r, c + 1, "E"))

        if neighbors:

            nr, nc, direction = random.choice(neighbors)

            remove_wall(r, c, nr, nc, direction)

            visited[nr][nc] = True
            stack.append((nr, nc))

        else:
            stack.pop()

        generate_maze()
        time.sleep(0.01)