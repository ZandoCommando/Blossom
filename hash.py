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

    