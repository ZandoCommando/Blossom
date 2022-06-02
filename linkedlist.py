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

    