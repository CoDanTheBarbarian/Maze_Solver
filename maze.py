import time
import random
from cell import Cell

class Maze:
    def __init__(
            self,
            x_1,
            y_1,
            num_rows,
            num_columns,
            cell_x_size,
            cell_y_size,
            win=None,
    ):
        self.x_1 = x_1
        self.y_1 = y_1
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_x_size = cell_x_size
        self.cell_y_size = cell_y_size
        self.win = win
        self._cells = []
        
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self.num_columns):
            cell_column = []
            for j in range(self.num_rows):
                cell_column.append(Cell(self.win))
            self._cells.append(cell_column)
        for i in range(self.num_columns):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        cell_x1 = self.x_1 + i * self.cell_x_size
        cell_y1 = self.y_1 + j * self.cell_y_size
        cell_x2 = cell_x1 + self.cell_x_size
        cell_y2 = cell_y1 + self.cell_y_size
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)


