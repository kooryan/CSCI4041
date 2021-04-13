# Hash Table
from collections import deque


class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def print_table(self):
        print(self.hash_table)

    def create_buckets(self):
        return [deque() for _ in range(self.size)]

    def search(self, key):
        index = 0
        for i in range(len(key)):
            index += i
        index %= self.size
        data = self.hash_table[index]

        for elem in data:
            record_key = elem[0]
            record_val = elem[1]

            if record_key == key:
                return record_val

        return "none"

    def insert(self, key, value):
        obj = self.search(key)

        index = 0
        for i in range(len(key)):
            index += i
        index %= self.size
        elem = [key, value]

        data = self.hash_table[index]
        if obj is "none":
            data.append(elem)
        else:
            for elem in data:
                if elem[0] == key:
                    elem[1] = value


hash_table = HashTable(100) # Setting the size and "m" for our Hash

hash_table.insert("bob", 99)
hash_table.insert("sally", 109)
# print(hash_table.search("bob"))
hash_table.insert("bob", 100)
print(hash_table.search("bob"))

hash_table.print_table()
