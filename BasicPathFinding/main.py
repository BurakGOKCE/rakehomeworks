"""

    ITU Robotic Search And Rescue

    Basic Path Finding Algorithm
    
    Definitions:

        - You are expected to design an algorithm that finds
        a path in order to escape from the maze

        - Maze is kind of a 2D map with one entry point
        and one exit point

        - Stack is a simple data structure which stores the data in
        form of LIFO (Last In First Out). For example, plates
        are stored as stacks. For further detail, check out the file
        "stack.py" under "classes" directory

        - Point is a custom data structure which has 3 attributes;
        x, y and next. This structure will be used to record the path
        currently passed. For further detail, check out the file
        "point.py" under "classes" directory

    Implementation Details:

        - You do not have to deal with generating the maze
        by reading data from the input file

        - You do not have to deal with implementing a stack,
        however it will be used in the algorithm. Check out the file
        stack.py under the classes directory for further detail

        - You do not have to implement the Point class, but you
        should use it in the algorithm for recording your moves.

        - You should implement a class for the algorithm (for example,
        a class named Algorithm) and run it in the "main.py"

"""

from classes import Algorithm

FILE_PATH = "resources\\mapdata.txt" # it is a relative path, you should use absolute path

if __name__ == "__main__":
    mazeAlgorithm = Algorithm(FILE_PATH)
    mazeAlgorithm.run()
