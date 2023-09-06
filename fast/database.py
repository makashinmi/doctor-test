class Database:
    def __init__(self):
        self.storage = {} 
        self.reversed_storage = {}

    def counts(self, value):
        return len(self.find(value))

    def debug(self):
        return f"{self.__class__=}\n{self.storage=}\n{self.reversed_storage=}"

    def find(self, value):
        try:
            return self.reversed_storage[value]
        except KeyError:
            return list()

    def get(self, key):
        try:
            return self.storage[key] 
        except KeyError:
            return 'NULL'

    def set(self, key, value):
        if key in self.storage:
            old_value = self.storage.pop(key)
            self.reversed_storage[old_value].remove(key)
            if len(self.reversed_storage[old_value]) == 0:
                self.reversed_storage.pop(old_value)
        self.storage[key] = "'NULL'" if value == 'NULL' else value
        try:
            self.reversed_storage[value].append(key) 
        except KeyError:
            self.reversed_storage[value] = [key]

    def unset(self, key):
        value = self.storage[key]
        self.storage.pop(key)
        self.reversed_storage.pop(value)



class Transaction(Database):
    def __init__(self, database_obj):
        super().__init__()
        self.parent = database_obj
        self.storage = database_obj.storage.copy()
        self.reversed_storage = database_obj.reversed_storage.copy()

    def commit(self):
        self.parent.storage = self.storage
        self.parent.reversed_storage = self.reversed_storage
