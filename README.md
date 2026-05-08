# https://www.loom.com/share/3e44975d62cd47f39cd1d94088b04520 This is my Loom link for the final result of the maze generator project.

# Maze Generator & Solver (DFS+Backtracking)

Project made for Python visualization purposes, where a maze is created and solved using the Depth-First Search (DFS) algorithm and backtracking.

Maze generation ("eating walls by the mouse"), maze solving, dead end detection, drawing walls dynamically and bonus cycles generating mode can be demonstrated with the help of Python’s standard module – turtle graphics.

---

# Features 

## Maze Generation
A dynamic maze creation using such techniques as:
- Depth-First Search (DFS)
- Stack based backtracking
- Neighbor cells choosing randomly

Orange mouse walks through the maze and destroys walls between cells.

---

## Maze Solver 
Red mouse tries to find the way from start cell to exit.

The solver:
- searches through possible paths
- backtracks on dead ends
- paints dead ends in blue squares

## Bonus feature: cycles
Usually, when using DFS technique, generated maze is called a perfect maze because there is one unique path between cells.

In this project, there is an additional functionality to create mazes
