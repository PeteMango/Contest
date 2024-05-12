from abc import ABC


class InMemoryDB(ABC):
    """
    `InMemoryDB` interface.
    """

    def set(self, key: str, field: str, value: str) -> None:
        """
        Should insert a `field`-`value` pair to the record
        associated with `key`.
        If the `field` in the record already exists, replace the
        existing value with the specified `value`.
        If the record does not exist, create a new one.
        """
        # default implementation
        pass

    def get(self, key: str, field: str) -> str | None:
        """
        Should return the value contained within `field` of the
        record associated with `key`.
        If the record or the `field` doesn't exist, should return
        `None`.
        """
        # default implementation
        return None

    def delete(self, key: str, field: str) -> bool:
        """
        Should remove the `field` from the record associated with
        `key`.
        Returns `True` if the field was successfully deleted, and
        `False` if the `key` or the `field` do not exist in the
        database.
        """
        # default implementation
        return False
