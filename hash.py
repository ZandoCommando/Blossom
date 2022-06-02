from node import Node
from linkedlist import LinkedList

class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for x in range(self.array_size)]

    