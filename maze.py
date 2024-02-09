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
            seed=None,
    ):
        self.x_1 = x_1
        self.y_1 = y_1
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_x_size = cell_x_size
        self.cell_y_size = cell_y_size
        self.win = win
        self._cells = []
        if seed:
            self._seed = seed
        else:
            self._seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

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

    def _break_walls_r(self, i, j):
        # catch the current cell in a variable based on the values i and j. This could be removed and self._cells[i][j] could be used in it's place, maybe this would save memory?
        current_cell = self._cells[i][j]
        # mark the current cell as having been visited
        current_cell.visited = True
        # start an infinite loop
        while True:
            # create an empty list to catch the unvisited cells
            to_visit = []
            # Check if Left cell exists and has not been visited
            if i > 0 and self._cells[i - 1][j].visited is False:
                    to_visit.append((i - 1, j, "L")) # storing the index values instead of the cell object, plus a directional character
            # Check if Right cell exists and has not been visited
            if i < self.num_columns - 1 and self._cells[i + 1][j].visited is False:
                    to_visit.append((i + 1, j, "R"))
            # Check in Bottom cell exists and had not been visited
            if j > 0 and self._cells[i][j - 1].visited is False:
                    to_visit.append((i, j - 1, "U")) # had this as down before - was mixed up
            # Check if Top cell exists and has not been visited
            if j < self.num_rows - 1 and  self._cells[i][j + 1].visited is False:
                    to_visit.append((i, j + 1, "D"))
            # Check if the to visit list is empty, thought the if not statement was doing that, don't think that's true
            if len(to_visit) == 0:
                # if so draw the current cell
                current_cell.draw(current_cell.x_1, current_cell.y_1, current_cell.x_2, current_cell.y_2)
                # check to see if any of the cells have not been visited
                for cols in self._cells:
                    for rows in cols:
                        # if it finds any that haven't been visited than call the break_walls_r method on that cell
                        if self._cells[cols][rows].visited is False:
                            self._break_walls_r(cols, rows) # fixed that. that was not how you call that method
                    # if you don't find any cells that haven't been visited then stop the loop
                return
            # If the visited list is not empty
            else:
                # generate a random number based on how many items are in the list
                random_direction = random.randrange(len(to_visit))
                # use that number minus one to represent the index of that list item and assign it to a variable
                random_cell = to_visit[random_direction]
                # match the caught directional character to the wall to destroy
                if random_cell[2] == "L":
                    current_cell.has_left_wall = False
                    self._cells[random_cell[0]][random_cell[1]].has_right_wall = False # didn't think about the fact the every inner wall is actually two walls, one for each Cell.
                if random_cell[2] == "R":
                    current_cell.has_right_wall = False
                    self._cells[random_cell[0]][random_cell[1]].has_left_wall = False
                if random_cell[2] == "D":
                    current_cell.has_bottom_wall = False
                    self._cells[random_cell[0]][random_cell[1]].has_top_wall = False
                if random_cell[2] == "U":
                    current_cell.has_top_wall = False
                    self._cells[random_cell[0]][random_cell[1]].has_bottom_wall = False
                # draw the current cell with it's new has_wall values
                current_cell.draw(current_cell.x_1, current_cell.y_1, current_cell.x_2, current_cell.y_2)
                # call the creak walls function on the coordinates of our random cell
                self._break_walls_r(random_cell[0], random_cell[1])
        