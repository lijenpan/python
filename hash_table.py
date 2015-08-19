import sys

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    table_size = 0
    entries_count = 0
    alphabet_size = 2 * 26
    hash_table = []


    def __init__(self, size):
        self.table_size = size
        self.hash_table = [[] for _ in xrange(size)]

    def hashing(self, key):
        hash = 0
        for i, c in enumerate(key):
            hash += self.alphabet_size ** (len(key) - i - 1) * (ord(c) - 65 - 7)
        return hash % self.table_size

    def insert(self,item):
        hash = self.hashing(item.key)
        for i,it in enumerate(self.hash_table[hash]):
            if it.key == item.key:
                del self.hash_table[hash][i]
                self.entries_count -= 1
        self.hash_table[hash].append(item)
        self.entries_count += 1

    def get(self,key):
        hash = self.hashing(key)
        for i, it in enumerate(self.hash_table[hash]):
            if it.key == key:
                return self.hash_table[hash]
        raise KeyError("Key is not in the table.")

    def delete(self,key):
        hash = self.hashing(key)
        for i, it in enumerate(self.hash_table[hash]):
            if it.key == key:
                del self.hash_table[hash][i]
                self.entries_count -= 1
                return
        raise KeyError("Key is not in the table.")

    def getNumEntries(self):
        return self.entries_count
