"""
    Point Class

    Attributes:
        - _x: represents the x coordinate of the point
        - _y: represents the y coordinate of the point
        - _next: represents the next Point object in the record

    Methods:
        - there are just simple getters and setters
        
    Usage:
        - it stores the x and y coordinates of the points visited
        - it also stores the next point in the record, which is
        previously visited

    Note:
        - you can use the operator == like (Point(x0,y0) == Point(x1,y1))

"""

class Point:
    def __init__(self, row, col) -> None:
        self._row = row
        self._col = col
        self._next = None

    def __eq__(self, pointIn) -> bool:
        if pointIn == None: return False
        elif self._row == pointIn.getRow() and self._col == pointIn.getCol(): return True
        else: False

    def getRow(self):
        return self._row

    def getCol(self):
        return self._col

    def getNext(self):
        return self._next

    def setRow(self, row):
        self._row = row

    def setCol(self, col):
        self._col = col

    def setNext(self, next):
        self._next = next
