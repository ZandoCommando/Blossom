from node import Node
from linkedlist import LinkedList

class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for x in range(self.array_size)]

    def __repr__(self):
        returnStr = ""
        for i in self.array:
            current = i.head
            while current is not None:
                returnStr += str(current.get_value().get_value()) + "\t"
                current = current.get_next_node()
            returnStr += "\n"

        return returnStr

    def hash(self, key):
        code = key.encode()
        finalHash = sum(code)
        return finalHash

    def compressor(self, hashOf):
        return hashOf % self.array_size

    def assign(self, key, value):
        hash_code = self.compressor(self.hash(key))
        list_at = self.array[hash_code]
        current = list_at.head
        while current is not None:
            value = current.get_value().get_value()
            if value[0] == key:
                value[1] = value

            current = current.get_next_node()

        list_at.insert_beginning(Node([key, value]))

    def retrieve(self, key):
        hash_code = self.compressor(self.hash(key))
        list_at = self.array[hash_code]
        current = list_at.head
        while current is not None:
            value = current.get_value().get_value()
            if value[0] == key:
                return value[1]

            current = current.get_next_node()

        return None