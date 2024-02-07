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
    def __init__(self, point_1, point_2, canvas, top=True, left=True, bottom=True, right=True,):
        self.x_1 = point_1.x
        self.y_1 = point_1.y
        self.x_2 = point_2.x
        self.y_2 = point_2.y
        self.has_top_wall = top
        self.has_left_wall = left
        self.has_bottom_wall = bottom
        self.has_right_wall = right
        self.win = canvas

    def draw_cell(self):
        top_left_point = Point(self.x_1, self.y_1)
        top_right_point = Point(self.x_2, self.y_1)
        bottom_right_point = Point(self.x_2, self.y_2)
        bottom_left_point = Point(self.x_1, self.y_2)
        if self.has_top_wall:
            top = Line(top_left_point, top_right_point)
            top.draw(self.win, "red")
        if self.has_left_wall:
            left = Line(top_left_point, bottom_left_point)
            left.draw(self.win, "red")
        if self.has_bottom_wall:
            bottom = Line(bottom_left_point, bottom_right_point)
            bottom.draw(self.win, "red")
        if self.has_right_wall:
            right = Line(top_right_point, bottom_right_point)
            right.draw(self.win, "red")

    def draw_move(self, to_cell, undo=False):
        point_1 = Point((self.x_1 + self.x_2) / 2, (self.y_1 + self.y_2) / 2)
        point_2 = Point((to_cell.x_1 + to_cell.x_2) / 2, (to_cell.y_1 + to_cell.y_2) / 2)
        foreward_path = Line(point_1, point_2)
        reverse_path = Line(point_2, point_1)
        if not undo:
            foreward_path.draw(self.win, "red")
        else:
            reverse_path.draw(self.win, "gray")

def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()