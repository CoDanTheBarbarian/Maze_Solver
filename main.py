from maze import Maze
from graphics import Window
import sys

def main():
    num_columns = 16
    num_rows = 12
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_x_size = (screen_x - 2 * margin) / num_columns
    cell_y_size = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)
    
    maze = Maze(margin, margin, num_rows, num_columns, cell_x_size, cell_y_size, win)
    print("Maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("Maze is unsolvable")
    else:
        print("Maze is solvable")
    win.wait_for_close()

if __name__ == "__main__":
    main()