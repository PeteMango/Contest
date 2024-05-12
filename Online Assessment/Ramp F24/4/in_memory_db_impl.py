from collections import defaultdict
from typing import Tuple, List, Optional
from typing_extensions import DefaultDict


class InMemoryDBImpl:

    def __init__(self):
        # d[key][field][(value, start_time, ttl)]
        # to be backwards compatible -1 means previous version
        self.db: DefaultDict[str, DefaultDict[str, Tuple[str, int, int]]] = defaultdict(lambda: defaultdict(lambda: ("", -1, -1)))

    def __isAlive(self, key: str, field: str, timestamp: int) -> bool:
        start, ttl = self.db[key][field][1], self.db[key][field][2]

        if start == -1:
            return True

        if ttl == -1:
            return start < timestamp

        return start < timestamp and timestamp < start + ttl

    def set(self, key: str, field: str, value: str) -> None:
        self.db[key][field] = (value, -1, -1)

    def set_at(self, key: str, field: str, value: str, timestamp: int) -> None:
        self.db[key][field] = (value, timestamp, -1)

    def set_at_with_ttl(self, key: str, field: str, value: str, timestamp: int, ttl: int) -> None:
        self.db[key][field] = (value, timestamp, ttl)

    def get(self, key: str, field: str) -> str | None:
        if key not in self.db or field not in self.db[key]:
            return None

        return self.db[key][field][0]

    def get_at(self, key: str, field: str, timestamp: int) -> str | None:
        if key in self.db and field in self.db[key]:
            value, start, ttl = self.db[key][field]

            if start == -1 or self.__isAlive(key, field, timestamp):
                return value

        return None

    def delete(self, key: str, field: str) -> bool:
        if key not in self.db or field not in self.db[key]:
            return False

        del self.db[key][field]
        return True

    def delete_at(self, key: str, field: str, timestamp: int) -> bool:
        if key in self.db and field in self.db[key]:
            if self.db[key][field][1] == -1 or self.__isAlive(key, field, timestamp):
                del self.db[key][field]
                return True

        return False

    def scan(self, key: str) -> List[str]:
        if key not in self.db:
            return []

        return [f'{field}({self.db[key][field][0]})' for field in sorted(self.db[key])]

    def scan_at(self, key: str, timestamp: int) -> List[str]:
        if key not in self.db:
            return []

        return [f'{field}({self.db[key][field][0]})' for field in sorted(self.db[key]) if self.__isAlive(key, field, timestamp) or self.db[key][field][1] == -1]

    def scan_by_prefix(self, key: str, prefix: str) -> List[str]:
        if key not in self.db:
            return []

        return [f'{field}({self.db[key][field][0]})' for field in sorted(self.db[key]) if field.startswith(prefix)]

    def scan_by_prefix_at(self, key: str, prefix: str, timestamp: int) -> List[str]:
        if key not in self.db:
            return []

        return [f'{field}({self.db[key][field][0]})' for field in sorted(self.db[key]) if field.startswith(prefix) and self.__isAlive(key, field, timestamp) or self.db[key][field][1] == -1]
