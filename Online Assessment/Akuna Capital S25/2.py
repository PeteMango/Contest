import os
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Caller(object):
    name: str


class CommsHandlerABC(ABC):
    @abstractmethod
    def connect(self, user1: Caller, user2: Caller) -> str:
        """implement connect method"""

    @abstractmethod
    def hangup(self, user1: Caller, user2: Caller) -> str:
        """implement hangup method"""

    @abstractmethod
    def clear_all(self) -> None:
        """implement clear_all"""


"""
Templates for messages. Use these for copy/paste to avoid typing.

{user1.name} cannot connect with {user2.name}
Connection in use. Please try later
Connection established between {user1.name} and {user2.name}
{user1.name} cannot hangup with {user2.name}
{user1.name} and {user2.name} not found in the communication channel
{user1.name} and {user2.name} are disconnected
"""


class ConnectionException(Exception):
    """Implemen this exception class"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class CommsHandler(CommsHandlerABC):
    """implement this class"""

    def __init__(self):
        self.inuse = False
        self.active_connections = []

    def connect(self, user1: Caller, user2: Caller) -> str:
        if user1 == user2:
            raise ConnectionException(f"{user1.name} cannot connect with {user2.name}")
        if self.inuse:
            raise ConnectionException("Connection in use. Please try later")

        self.active_connections.append(user1)
        self.active_connections.append(user2)
        self.inuse = True

        return f"Connection established between {user1.name} and {user2.name}"

    def hangup(self, user1: Caller, user2: Caller) -> str:
        if user1 == user2:
            raise ConnectionException(f"{user1.name} cannot hangup with {user2.name}")

        if user1 not in self.active_connections or user2 not in self.active_connections:
            raise ConnectionException(
                f"{user1.name} and {user2.name} not found in the communication channel"
            )

        self.active_connections.clear()
        self.inuse = False
        return f"{user1.name} and {user2.name} are disconnected"

    def clear_all(self) -> None:
        self.inuse = False
        self.active_connections.clear()
        assert len(self.active_connections) == 0


def main(path="/dev/stdout") -> None:
    # Create Communication
    comms = CommsHandler()
    functions = {"connect": comms.connect, "hangup": comms.hangup}
    # Create users
    n = int(input().strip())
    users = []
    for i in range(n):
        name = input().strip()
        u = Caller(name)
        assert u.name == name
        users.append(u)

    result_str = ""
    # Perform operations
    instructions_count = int(input().strip())
    for i in range(instructions_count):
        instructions = input().strip().split()
        u1, u2 = map(int, instructions[1:])
        try:
            result_str += (
                "Success: " + functions[instructions[0]](users[u1], users[u2]) + "\n"
            )
        except ConnectionException as ce:
            result_str += "Error: " + str(ce) + "\n"
    comms.clear_all()
    assert len(comms.active_connections) == 0

    with open(path, "w") as fptr:
        fptr.write(result_str)


if __name__ == "__main__":
    path = "/dev/stdout"
    if "OUTPUT_PATH" in os.environ.keys():
        path = os.environ["OUTPUT_PATH"]
    main(path=path)
