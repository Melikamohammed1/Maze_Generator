import turtle
import random
import time

# ---------------- CONFIG ---------------- #
ROWS = 20
COLS = 25
CELL_SIZE = 24
BONUS_MODE = True      # Create cycles (bonus feature)
EXTRA_WALL_CHANCE = 20 # 1 in 20 chance

# ---------------- SCREEN ---------------- #
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Generator and Solver (DFS + Backtracking)")
wn.setup(1300, 700)
wn.tracer(0)

# ---------------- DRAWING TURTLE ---------------- #
wall_t = turtle.Turtle()
wall_t.hideturtle()
wall_t.speed(0)
wall_t.color("white")
wall_t.penup()


# ---------------- GENERATOR MOUSE ---------------- #
gen_mouse = turtle.Turtle()
gen_mouse.shape("circle")
gen_mouse.color("orange")
gen_mouse.penup()
gen_mouse.speed(0)

# ---------------- SOLVER MOUSE ---------------- #
solver_mouse = turtle.Turtle()
solver_mouse.shape("circle")
solver_mouse.color("red")
solver_mouse.penup()
solver_mouse.speed(0)

 # ---------------- DEAD END MARKER ---------------- #
dead_t = turtle.Turtle()
dead_t.shape("square")
dead_t.color("blue")
dead_t.penup()
dead_t.speed(0)
dead_t.shapesize(0.6)
        

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
            
            # BONUS:
            # Randomly remove extra walls to create cycles
            if BONUS_MODE and random.randint(1, EXTRA_WALL_CHANCE) == 1:

                extra_dirs = []

                if r > 0:
                    extra_dirs.append((r - 1, c, "N"))

                if r < ROWS - 1:
                    extra_dirs.append((r + 1, c, "S"))

                if c > 0:
                    extra_dirs.append((r, c - 1, "W"))

                if c < COLS - 1:
                    extra_dirs.append((r, c + 1, "E"))

                er, ec, edir = random.choice(extra_dirs)

                remove_wall(r, c, er, ec, edir)


            visited[nr][nc] = True
            stack.append((nr, nc))

        else:
            stack.pop()
           
        
        draw_maze()
        wn.update()
        time.sleep(0.01)

# ---------------- CAN MOVE ---------------- #
def can_move(r, c, direction):

    if direction == "N":
        return r > 0 and northWall[r][c] == 0

    elif direction == "S":
        return r < ROWS - 1 and northWall[r + 1][c] == 0

    elif direction == "E":
        return c < COLS - 1 and eastWall[r][c] == 0

    elif direction == "W":
        return c > 0 and eastWall[r][c - 1] == 0

    return False

# ---------------- SOLVE MAZE ---------------- #
def solve_maze(start, end):

    sr, sc = start
    er, ec = end

    stack = [(sr, sc)]

    visited_solver = set()
    visited_solver.add((sr, sc))

    while stack:

        r, c = stack[-1]

        x, y = cell_to_screen(r, c)

        solver_mouse.goto(
            x + CELL_SIZE / 2,
            y - CELL_SIZE / 2
        )

        wn.update()
        time.sleep(0.03)

        if (r, c) == (er, ec):
            print("Maze Solved!")
            return

        moves = []

        directions = ["N", "S", "E", "W"]
        random.shuffle(directions)

        for d in directions:

            if can_move(r, c, d):

                nr, nc = r, c

                if d == "N":
                    nr -= 1

                elif d == "S":
                    nr += 1

                elif d == "E":
                    nc += 1

                elif d == "W":
                    nc -= 1

                if (nr, nc) not in visited_solver:
                    moves.append((nr, nc))

        if moves:

            next_cell = random.choice(moves)

            visited_solver.add(next_cell)
            stack.append(next_cell)

        else:
            # Dead end -> mark blue
            dead_t.goto(
                x + CELL_SIZE / 2,
                y - CELL_SIZE / 2
            )
            
            stack.pop()
       




# ---------------- START AND END ---------------- #
start_row = random.randint(0, ROWS - 1)
end_row = random.randint(0, ROWS - 1)



# RUN PROGRAM

generate_maze()

eastWall[start_row][0] = 0
eastWall[end_row][COLS - 1] = 0

draw_maze()
wn.update()
# Start and end cells
start = (start_row, 0)
end = (end_row, COLS - 1)

# Solve maze
solve_maze(start, end)

turtle.done()



