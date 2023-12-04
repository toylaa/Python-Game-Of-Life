## Same as test1, but with grid.as_string function

## First, import the grid and patterns modules from the rplife package.
#from rplife import grid, patterns 
import grid, patterns 

## Then, you create a Pattern instance.
blinker = patterns.Pattern("Blinker", {(2,1), (2,2), (2,3)})

## Next up, you create a LifeGrid object.
grid = grid.LifeGrid(blinker)
## Note that when you print this object, you get the pattern’s name and live cells.
print(grid.as_string((0, 0, 5, 5)))
"""  
Blinker  
‧ ‧ ‧ ‧ ‧ 
‧ ‧ ‧ ‧ ‧ 
‧ ♥ ♥ ♥ ‧ 
‧ ‧ ‧ ‧ ‧ 
‧ ‧ ‧ ‧ ‧  
"""

## Evolve the grid by calling .evolve().
grid.evolve()
print(grid.as_string((0, 0, 5, 5)))
##  This time, you get a different set of living cells.
"""
 Blinker  
‧ ‧ ‧ ‧ ‧ 
‧ ‧ ♥ ‧ ‧ 
‧ ‧ ♥ ‧ ‧ 
‧ ‧ ♥ ‧ ‧ 
‧ ‧ ‧ ‧ ‧ 
"""


## If you evolve the grid again, then you get the same set of live cells
#   that you use as the initial seed for the game. 
## This is because the Blinker pattern is an oscillator pattern 
grid.evolve()
print(grid.as_string((0, 0, 5, 5)))
""" 
 Blinker
‧ ‧ ‧ ‧ ‧
‧ ‧ ‧ ‧ ‧
‧ ♥ ♥ ♥ ‧
‧ ‧ ‧ ‧ ‧
‧ ‧ ‧ ‧ ‧ 
"""