class Robot:
    """
    Robot class that models the movement of the rover
    """

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # maps to N, E, S, W respectively
    orientation = ['N', 'E', 'S', 'W']

    command = """Command the robot with:
        L - turn left
        R - turn right
        M - move forward
        ? - this message
        Q - quit"""
    
    shutdowns = """Robot shutting down."""

    def __init__(self):
        self.xcoord = 0
        self.ycoord = 0
        self.facing = 'N'

        print(f'Hello! Robot coming online.\n{self.command}')
    
    def __turn(self, dir: str) -> None:
        if dir == 'L':
            self.facing = self.orientation[(self.orientation.index(self.facing) - 1) % 4]
            return

        self.facing = self.orientation[(self.orientation.index(self.facing) + 1) % 4]

        
    def __move(self) -> None:
        self.xcoord, self.ycoord = self.xcoord + self.direction[self.orientation.index(self.facing)][0], self.ycoord + self.direction[self.orientation.index(self.facing)][1]
    
    def __repr__(self):
        return f'Rover at ({self.xcoord}, {self.ycoord}) facing {self.facing}'

    def handle(self, cmd: str) -> None:
        if cmd in ('L', 'R'):
            self.__turn(cmd)
        elif cmd == 'M':
            self.__move()
        elif cmd == 'Q':
            print(self.shutdowns)
            exit(0)
        else:
            print(f'Invalid command:\n{self.command}')
        print(self)

def handle() -> None:
    rover = Robot()
    while True:
        command = input()
        rover.handle(command)
    
if __name__ == "__main__":
    handle()