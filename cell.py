from graphics import Point,Line

class Cell:
    def __init__(self, win=None):
        self.x_1 = None
        self.y_1 = None
        self.x_2 = None
        self.y_2 = None
        self.has_top_wall = True
        self.has_left_wall = True
        self.has_bottom_wall = True
        self.has_right_wall = True
        self.win = win
        self.visited = False

    def draw(self, x_1, y_1, x_2, y_2):
        if self.win is None:
            return
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2
        if self.has_top_wall:
            top = Line(Point(x_1, y_1), Point(x_2, y_1))
            top.draw(self.win, "black")
        else:
            top = Line(Point(x_1, y_1), Point(x_2, y_1))
            top.draw(self.win, "white")
        if self.has_left_wall:
            left = Line(Point(x_1, y_1), Point(x_1, y_2))
            left.draw(self.win, "black")
        else:
            left = Line(Point(x_1, y_1), Point(x_1, y_2))
            left.draw(self.win, "white")
        if self.has_bottom_wall:
            bottom = Line(Point(x_1, y_2), Point(x_2, y_2))
            bottom.draw(self.win, "black")
        else:
            bottom = Line(Point(x_1, y_2), Point(x_2, y_2))
            bottom.draw(self.win, "white")
        if self.has_right_wall:
            right = Line(Point(x_2, y_1), Point(x_2, y_2))
            right.draw(self.win, "black")
        else:
            right = Line(Point(x_2, y_1), Point(x_2, y_2))
            right.draw(self.win, "white")


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