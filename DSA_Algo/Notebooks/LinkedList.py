class Node:

    def __init__(self, data=None, reference=None):
        self.data = data
        self.reference = reference


class LinkedList:

    def __init__(self):
        self.head = None


n1 = Node('GOW')
n2 = Node('COD')
n3 = Node('GTA5')

ll = LinkedList()
# Node to be added at the beginning
n0 = Node('PUBG')

ll.head = n0
n0.reference = n1
n1.reference = n2
n2.reference = n3

pointer = ll.head
print('Head =>')

while pointer:
    print(pointer.data, end=' ')
    pointer = pointer.reference


