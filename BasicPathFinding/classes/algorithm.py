from .stack import Stack
from .point import Point

OBSTACLE = "x"
FINISH = "F"

class Algorithm:
    def __init__(self, fileName) -> None:
        self._file = open(fileName) # to read the data
        self._map = list() # to create a 2D array
        self._location = Point(0, 0) # initial point is always (0, 0)
        self._camefrom = None

    # Handled for you
    def generateMap(self):
        row_index = 0

        for line in self._file:
            charArray = line.strip("\n")
            self._map.append([])

            for each in charArray:
                self._map[row_index].append(each)

            row_index += 1

        return self._map

    """
        Different methods are optional (and very useful!)
    """

    def run(self):
        # write your code here
        pass
