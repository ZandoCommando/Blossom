from node import Node
from linkedlist import LinkedList

class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for x in range(self.array_size)]

    def hash(self, key):
        code = key.encode()
        finalHash = sum(code)
        return finalHash

    def compressor(self, hashOf):
        return hashOf % self.array_size

    def assign(self, key, value):
        hash_code = self.compressor(self.hash(key))
        list_at = self.array[hash_code]
        for item in list_at:
            if item[0] == key:
                item[1] = value

        item.insert_beginning(Node([key, value]))

    def retrieve(self, key):
        hash_code = self.compressor(self.hash(key))
        list_at = self.array[hash_code]
        for item in list_at:
            if item[0] == key:
                return item[1]

        return None