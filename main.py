from maze import Maze
from graphics import Window


def main():
    num_columns = 16
    num_rows = 12
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_x_size = (screen_x - 2 * margin) / num_columns
    cell_y_size = (screen_y - 2 * margin) / num_rows
    
    win = Window(screen_x, screen_y)
    
    maze = Maze(margin, margin, num_rows, num_columns, cell_x_size, cell_y_size, win, 10)

    win.wait_for_close()

if __name__ == "__main__":
    main()