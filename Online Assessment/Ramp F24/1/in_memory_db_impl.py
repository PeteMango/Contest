from in_memory_db import InMemoryDB
from collections import defaultdict
from typing import Tuple
from typing_extensions import DefaultDict


class InMemoryDBImpl(InMemoryDB):

    def __init__(self):
        self.db: DefaultDict[str, DefaultDict[str, str]] = defaultdict(lambda: defaultdict(str))

        pass

    def set(self, key: str, field: str, value: str) -> None:
        # print(f'set {self.db}')
        self.db[key][field] = value
        return

    def get(self, key: str, field: str) -> str | None:
        # print(f'get {self.db}')
        if key not in self.db or field not in self.db[key]:
            return None

        return self.db[key][field]

    def delete(self, key: str, field: str) -> bool:
        # print(f'delete {self.db}')
        if key not in self.db or field not in self.db[key]:
            return False

        del self.db[key][field]
        return True

    # TODO: implement interface methods here
