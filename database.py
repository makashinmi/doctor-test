class Database:
    def __init__(self):
        self.storage = {} 

    def counts(self, value: str) -> str:
        return len(self.find(value))

    def find(self, value: str) -> list:
        try:
            return self.__reverse_storage()[value]
        except KeyError:
            return list()

    def get(self, key: str) -> str:
        try:
            return "'NULL'" if self.storage[key] == 'NULL' else self.storage[key]
        except KeyError:
            return 'NULL'

    def set(self, key: str, value: str) -> None:
        if key in self.storage:
            self.storage.pop(key)
        self.storage[key] = value

    def unset(self, key: str) -> None:
        value = self.storage[key]
        self.storage.pop(key)

    def __debug(self, func):
        def wrapper(**args):
            print(f"{self.__class__=}\n{self.storage=}")
            return func(args)
        return wrapper 

    def __reverse_storage(self) -> dict:
        reversed_storage = {}
        for key, value in self.storage.items():
            if value in reversed_storage:
                reversed_storage[value].append(key)
            else:
                reversed_storage[value] = [key]
        return reversed_storage


class Transaction(Database):
    def __init__(self, database_obj):
        super().__init__()
        self.parent = database_obj
        self.storage = database_obj.storage.copy()

    def commit(self) -> None:
        self.parent.storage = self.storage 
