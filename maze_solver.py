# Maze Solver
from tkinter import Tk, BOTH, Canvas

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
        starting_x = (self.x_1 + self.x_2) / 2
        starting_y = (self.y_1 + self.y_2) / 2
        ending_x = (to_cell.x_1 + to_cell.x_2) / 2
        ending_y = (to_cell.y_1 + to_cell.y_2) / 2
        
        fill_color = "red"
        if undo:
            fill_color = "gray"
        
        line_forward = Line(Point(starting_x, starting_y), Point(ending_x, ending_y))
        line_forward.draw(self.win, fill_color)

def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()