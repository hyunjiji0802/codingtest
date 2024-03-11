class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        if pos == 1:
            result = self.head
            self.head = self.head.next
            if self.nodeCount == 1:
                self.tail = self.head

        elif pos == self.nodeCount:
            result = self.getAt(pos)
            prev = self.getAt(pos - 1)
            prev.next = self.tail.next
            self.tail = prev

        else:
            result = self.getAt(pos)
            prev = self.getAt(pos - 1)
            prev.next = prev.next.next

        self.nodeCount -= 1

        return result.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(10)

l = LinkedList()
l.insertAt(1,a)
l.insertAt(2,b)
l.insertAt(3,c)
l.insertAt(4,d)

print(l.traverse())
print(l.popAt(1))
print(l.traverse())
print(l.popAt(2))
print(l.traverse())

