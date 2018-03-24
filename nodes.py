class Node:

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):

        return self.data

    def setData(self, val):

        self.data = val

    def getNextNode(self)
        return self.nextNode

    def setNextNode(self, val):
        nextNode = (input("Enter your list of items"))
        self.nextNode = val
    

class LinkedList:

    def __init__(self,head = None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, data):
        newNode = Node(data, self.head)

        self.head = newNode
        self.size += 1
        return True

    def printNode(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.getNextNode()




# instantiate
myList = LinkedList()
newNode = Node(['cat','dog'])
print(newNode.getData())


print(newNode.getData())
# add nodes
print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(25))

# print the nodes
print("Printing")
myList.printNode()

# print the size of a node
print("Size")
print(myList.getSize())

data = [1,2,3]
myNode = Node(data)
