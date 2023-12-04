import collections

ALIVE = "♥"
DEAD = "‧"

class LifeGrid:

    def __init__(self, pattern):
        self.pattern = pattern

    ##----------------------------------------------------------------------------##
    
    def evolve(self):
        #define the delta coordinates for the neighbors of the target cell.
        neighbors = (
            (-1,-1) , #Above Left
            (-1, 0) , #Above 
            (-1, 1) , #Above right
            ( 0,-1) , #Left
            ( 0, 1) , #Right
            ( 1,-1) , #Below Left
            ( 1, 0) , #Below
            ( 1, 1) , #Below Right
        )

        ## Create a dictionary for counting the number of living neighbors. 
        ##   Use the defaultdict class from the collections module to build 
        #     the counter with the int class as its default factory.
        num_neighbors = collections.defaultdict(int)

        ## This loop allows us to Check the neighbors of each living cell 
        #   to determine the next generation of living cells.        
        for row, col in self.pattern.alive_cells:
        ## Loop over the currently alive cells stored in the .pattern object.
            for drow, dcol in neighbors:
            ## Loop over the neighbor deltas, count how many neighbors a cell has
                num_neighbors[(row+drow, col+dcol)] += 1

        ## Build a set containing the cells that will stay alive. 
        ## To do this, first create a set of neighbors that have two or three 
        #   alive neighbors themselves. Then, find the cells that are common 
        #   to both this set and .alive_cells.
        stay_alive = {
            cell for cell, num in num_neighbors.items() if num in {2, 3}
        } & self.pattern.alive_cells

        ## Create a set with the cells that will come alive.
        ## In this case, create a set of neighbors that have exactly three 
        #   living neighbors. Then, you determine the cells that come alive 
        #   by removing cells that are already in .alive_cells.
        come_alive = {
            cell for cell, num in num_neighbors.items() if num == 3
        } - self.pattern.alive_cells

        ## Updates .alive_cells with the set that results as the union of the 
        #   cells that stay alive and those that come alive
        self.pattern.alive_cells = stay_alive | come_alive

    ##----------------------------------------------------------------------------##

    def as_string(self, bbox):
        ## Unpack the bounding box coordinates into four variables. 
        ## These variables define which part of the infinite grid 
        #    to display on the screen.
        start_col, start_row, end_col, end_row = bbox
        
        ##Then, you create the display variable as a list containing the pattern’s name. 
        ## .center() is used here to center the name over the grid’s width.
        display = [self.pattern.name.center(2 * (end_col - start_col))]
        
        ## Iterate over the range of rows inside the view
        for row in range(start_row, end_row):
            ## Create a new list containing the alive and dead cells in the current row.
            display_row = [
                ## Check if its coordinates are in the set of alive cells
                ALIVE if (row, col) in self.pattern.alive_cells else DEAD
                for col in range(start_col, end_col)
            ]
            ## Append the row as a string to the display list
            display.append(" ".join(display_row))

        ##  After loop, join together every string using a newline character
        return "\n".join(display)

    ##----------------------------------------------------------------------------##

    ## The .__str__() special method provides a way to represent the 
    #    containing object in a user-friendly manner. 
    ## With this method in place, when you use the built-in print() function 
    #    to print an instance of LifeGrid, you get:
    #           - the name of the current pattern 
    #           - and the set of alive cells in the next line. 
    ## This information gives you an idea of the current state of the life grid.
    def __str__(self):
        return (
            f"{self.pattern.name}:\n"
            f"Alive Cells --> {sorted(self.pattern.alive_cells)}"
        )