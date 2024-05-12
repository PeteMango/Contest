from in_memory_db import InMemoryDB
from collections import defaultdict
from typing import Tuple, List
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

    def scan(self, key: str) -> List[str]:
        if key not in self.db:
            return []

        fields = []
        for field, value in self.db[key].items():
            fields.append(field)

        fields.sort()
        ret = []
        for field in fields:
            ret.append(f'{field}({self.db[key][field]})')

        return ret

    def scan_by_prefix(self, key:str, prefix: str) -> List[str]:
        if key not in self.db:
            return []

        fields = []
        for field, value in self.db[key].items():
            if field.startswith(prefix):
                fields.append(field)

        fields.sort()
        ret = []
        for field in fields:
            ret.append(f'{field}({self.db[key][field]})')

        return ret

    # TODO: implement interface methods here
