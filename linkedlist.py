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

    def remove_by_value(self, value):
        current = self.head
        if current.get_value() == value:
            self.head = current.get_next_node()
        else:
            prev = current
            current = current.get_next_node()
            while current is not None:
                if current.get_value() == value:
                    prev.set_next_node(current.get_next_node())
                    break

                prev = current
                current = current.get_next_node()

            