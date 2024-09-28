"""Mars rover challenge
"""

class Grid:
    """Stores the grid that the rover will travel on
    """

    def __init__(self, xsize, ysize: int):
        self.xsize = xsize
        self.ysize = ysize

    def handle(self):
        """handle input and print output
        """
        x, y, d = input().split(' ')
        x, y = int(x), int(y)
        c = input()

        r = Rover(x, y, d)
        r.execute_command(c, self.xsize, self.ysize)

        print(f'{r.curx} {r.cury} {r.orientation}')

class Rover:
    """stores individual rovers
    """

    def __init__(self, startx, starty: int, initial_dir: str):
        self.curx = startx
        self.cury = starty
        self.orientation = initial_dir
        self.directions = [
            ('N', (0, 1)), ('E', (1, 0)), ('S', (0, -1)), ('W', (-1, 0))
        ]

    def __rotate(self, direction: str):
        """Rotate the current orientation of the rover

        Args:
            dir (str): either 'L' or 'R' signaling which direction to move
        """
        idx = 0
        for i, (d, (_, _)) in enumerate(self.directions):
            if d == self.orientation:
                idx = i
                break

        if direction == 'L':
            self.orientation = self.directions[(idx - 1) % 4][0]
        else:
            self.orientation = self.directions[(idx + 1) % 4][0]

    def __move(self, xsize, ysize: int):
        """Moves the robot forward based on current orientation
        """

        x, y = 0, 0
        for d, (dx, dy) in self.directions:
            if d == self.orientation:
                x, y = dx, dy
                break

        nx, ny = self.curx + x, self.cury + y

        # if outside of grid, do nothing
        if nx > xsize or nx < 0 or ny > ysize or ny < 0:
            return

        self.curx, self.cury = nx, ny


    def execute_command(self, c: str, xsize: int, ysize: int):
        """Moves the robot based on the command

        Args:
            c (str): the string of commands
            xsize (int): size of the x direction of the grid
            ysize (int): size of the y direction of the grid
        """

        for cmd in c:
            if cmd == 'L' or cmd == 'R':
                self.__rotate(cmd)
            else:
                self.__move(xsize, ysize)

def run():
    """Runs the entire program
    """
    xsize, ysize = map(int, input().split(' '))
    g = Grid(xsize, ysize)

    for _ in range(2):
        g.handle()

run()
