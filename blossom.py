from flowers import flower_definitions
from hash import HashMap
from node import Node
from linkedlist import LinkedList


blossoms = HashMap(len(flower_definitions))
for item in flower_definitions:
    blossoms.assign(item[0], item[1])

print(blossoms)

print(blossoms.retrieve('rose'))
print(blossoms.retrieve('lavender'))
print(blossoms.retrieve('morning glory'))