class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printing(self):
        printValue = self.head
        while printValue is not None:
            print(printValue.data)
            printValue = printValue.next

    def beg(self, data4):
        new = Node(data4)
        new.next = self.head
        self.head = new

    def end(self, data5):
        newest = Node(data5)
        if self.head is None:
            self.head = newest
            return
        lastNode = self.head
        while (lastNode.next):
            lastNode = lastNode.next
        lastNode.next = newest

    def between(self,node,datapart):
        newofall = Node(datapart)
        newofall.next = node.next
        node.next = newofall

x = LinkedList()
x.head = Node("John Bakly")
data2 = Node("Soni Roy")
data3 = Node("Udemy")

x.head.next = data2
data2.next = data3


x.beg("Tutorials")
x.beg("insert")
x.end("Anything")
x.end("Insert")
x.between(x.head.next.next,"between")
x.printing()

