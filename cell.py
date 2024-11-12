from graphics import Point,Line

class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_top_wall = True
        self.has_left_wall = True
        self.has_bottom_wall = True
        self.has_right_wall = True
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_top_wall:
            top = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top, "black")
        else:
            top = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top, "white")
        if self.has_left_wall:
            left = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left, "black")
        else:
            left = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left, "white")
        if self.has_bottom_wall:
            bottom = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom, "black")
        else:
            bottom = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom, "white")
        if self.has_right_wall:
            right = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right, "black")
        else:
            right = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right, "white")


    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        half_length = abs(self._x2 - self._x1) // 2
        starting_x = self._x1 + half_length
        starting_y = self._y1 + half_length
        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        ending_x = to_cell._x1 + half_length2
        ending_y = to_cell._y1 + half_length2
        
        fill_color = "red"
        if undo:
            fill_color = "gray"
        
        line = Line(Point(starting_x, starting_y), Point(ending_x, ending_y))
        self._win.draw_line(line, fill_color)