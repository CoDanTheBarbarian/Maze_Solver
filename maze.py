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