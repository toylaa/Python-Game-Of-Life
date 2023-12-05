from dataclasses import dataclass
from pathlib import Path

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"

## To parse a TOML file and read its content into Python objects,
#  if you’re using Python 3.11 or later, you can use the standard-library module tomllib . 
# Otherwise, you should use the third-party library tomli, which is compatible with tomllib.
try:
    import tomllib
except ImportError:
    import tomli as tomllib


@dataclass
class Pattern: 
    name: str 
    alive_cells: set[tuple[int, int]]


    ## Class methods are great when you need to provide an alternative
    #   constructor in a class. 
    ## These types of methods receive the current class as their first argument, 
    #   "cls" .
    @classmethod
    def from_toml(cls, name, toml_data):
        ## Create and return an instance of the class using the cls argument. 
        return cls(
            name,
            alive_cells = {tuple(cell) for cell in toml_data["alive_cells"]},            
        )
    ## Create a set of tuples from the list of lists that you get from the TOML file. 
            ## Each tuple will contain the coordinates of a living cell on the life grid.
            ## Note that to access the alive cells in the TOML data,
            #   you can use the dictionary lookup notation with the name  
            #    of the target key in square brackets.

    
def get_pattern(name, filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return Pattern.from_toml(name, toml_data=data[name])

def get_all_patterns(filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return [
        Pattern.from_toml(name, toml_data) for name, toml_data in data.items()
    ]