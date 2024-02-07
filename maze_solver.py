# Maze Solver
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.title = ""
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack(expand=1, fill=BOTH)
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running is True:
            self.redraw()

    def close(self):
        self.running = False

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


def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()