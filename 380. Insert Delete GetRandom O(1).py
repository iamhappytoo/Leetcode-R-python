class RandomizedSet:

    def __init__(self):
        self.table = {}
        self.myset = set()

    def insert(self, val: int) -> bool:
        if val in self.table:
            return False
        else:
            self.table[val] = 1
            self.myset.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.table:
            self.myset.remove(val)
            self.table.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.sample(self.myset,1)[0]
