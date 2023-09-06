class Database:
    def __init__(self):
        self.storage = {} 

    def counts(self, value):
        return len(self.find(value))

    def find(self, value):
        try:
            return self.__reverse_storage()[value]
        except KeyError:
            return list()

    def get(self, key):
        try:
            return self.storage[key] 
        except KeyError:
            return 'NULL'

    def set(self, key, value):
        if key in self.storage:
            self.storage.pop(key)
        self.storage[key] = "'NULL'" if value == 'NULL' else value

    def unset(self, key):
        value = self.storage[key]
        self.storage.pop(key)

    def __debug(self, func):
        def wrapper(**args):
            print(f"{self.__class__=}\n{self.storage=}")
            return func(args)
        return wrapper 

    def __reverse_storage(self):
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

    def commit(self):
        self.parent.storage = self.storage 
