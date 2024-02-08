# Maze Solver
from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(self.root, width=self.width, height=self.height)
        self.__canvas.pack(expand=1, fill=BOTH)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running is True:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, color):
        line.draw(self.canvas, color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2
        )
        canvas.pack(expand=1, fill=BOTH)
        
class Cell:
    def __init__(self, win):
        self.x_1 = None
        self.y_1 = None
        self.x_2 = None
        self.y_2 = None
        self.has_top_wall = True
        self.has_left_wall = True
        self.has_bottom_wall = True
        self.has_right_wall = True
        self.win = win

    def draw_cell(self, x_1, y_1, x_2, y_2):
        if self.win is None:
            return
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2
        if self.has_top_wall:
            top = Line(Point(x_1, y_1), Point(x_2, y_1))
            top.draw(self.win, "black")
        if self.has_left_wall:
            left = Line(Point(x_1, y_1), Point(x_1, y_2))
            left.draw(self.win, "black")
        if self.has_bottom_wall:
            bottom = Line(Point(x_1, y_2), Point(x_2, y_2))
            bottom.draw(self.win, "black")
        if self.has_right_wall:
            right = Line(Point(x_2, y_1), Point(x_2, y_2))
            right.draw(self.win, "black")

    def draw_move(self, to_cell, undo=False):
        if self.win is None:
            return
        starting_x = (self.x_1 + self.x_2) / 2
        starting_y = (self.y_1 + self.y_2) / 2
        ending_x = (to_cell.x_1 + to_cell.x_2) / 2
        ending_y = (to_cell.y_1 + to_cell.y_2) / 2
        
        fill_color = "red"
        if undo:
            fill_color = "gray"
        
        line_forward = Line(Point(starting_x, starting_y), Point(ending_x, ending_y))
        line_forward.draw(self.win, fill_color)

class Maze:
    def __init__(
            self,
            x_1,
            y_1,
            num_rows,
            num_columns,
            cell_x_size,
            cell_y_size,
            win,
    ):
        self.x_1 = x_1
        self.y_1 = y_1
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_x_size = cell_x_size
        self.cell_y_size = cell_y_size
        self.win = win
        self._cells = []

    def _create_cells(self):
        for i in range(self.num_columns):
            cell_column = []
            for j in range(self.num_rows):
                cell = Cell(self.win)
                cell_column.append(cell)
            self._cells.append(cell_column)
        for i in self.num_columns:
            for j in self.num_rows:
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        cell_x1 = self.x_1 + i * self.cell_x_size
        cell_y1 = self.y_1 + j * self.cell_y_size
        cell_x2 = cell_x1 + self.cell_x_size
        cell_y2 = cell_y1 + self.cell_y_size
        self.cells[i][j].draw_cell(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(.05)








def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()