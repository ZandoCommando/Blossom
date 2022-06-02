from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        returnStr = ""
        current = self.head
        while current is not None:
            returnStr += str(current.get_value()) + "\n"
            current = current.get_next_node()

        return returnStr

    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head)
        self.head = new_node

        