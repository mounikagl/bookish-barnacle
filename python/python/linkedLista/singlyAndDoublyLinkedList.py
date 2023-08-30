class Node:
    def __init__(self, dataValue = None):
        self.dataValue = dataValue
        self.nextValue = None

class linkedList:
    def __init__(self):
        self.headValue = None

    def printing(self):
        printvalue = self.headValue
        while printvalue is not None:
            if(printvalue.dataValue == "Udemy"):
                print(printvalue.dataValue)
                printvalue = printvalue.nextValue
            else:
                printvalue = printvalue.nextValue
    
x = linkedList()
x.headValue = Node('John Barley')
data2 = Node('Bake cipher')
data3 = Node('udemy')

x.headValue.nextValue = data2
data2.nextValue = data3

x.printing()