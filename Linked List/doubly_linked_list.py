class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def setdata(self, data):
        self.data = data

    def getdata(self):
        return self.data

    def setnext(self, next):
        self.next = next

    def getnext(self):
        return self.next

    def setprev(self, prev):
        self.prev = prev

    def getprev(self):
        return self.prev


class DoublyLinkedlist:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insertatfirst(self, data):
        newnode = Node()
        newnode.setdata(data)

        if self.head is None:
            self.head = self.tail = newnode
        else:
            newnode.setprev(None)
            newnode.setnext(self.head)
            self.head.setprev(newnode)
            self.head = newnode
        return self.head.data

    def insertatlast(self, data):
        newnode = Node()
        newnode.setdata(data)

        if self.head is None:
            self.head = self.tail = newnode

        else:
            newnode.setnext(None)
            newnode.setprev(self.tail)
            self.tail.setnext(newnode)
            self.tail = newnode
        return self.tail.data

    def displaydata(self):
        current = self.head
        count = 0
        while current:
            print(current.data)
            count = count + 1
            current = current.getnext()
        return "Count", count

    def insertatposition(self, data, pos):
        newnode = Node()
        newnode.setdata(data)

        current = self.head
        if pos == 0:
            raise Exception("Please enter correct position")
        elif pos == 1:
            return self.insertatfirst(data)
        else:
            while current == pos - 1:
                current = current.getnext()
            newnode.setnext(current.getnext())
            newnode.setprev(current.getprev())
            current.setnext(newnode)
            current.getnext().setprev(newnode)
            return "sucessfully"

    def deletefromstart(self):
        if self.head == self.tail:
            self.head=self.tail=None
        self.head = self.head.getnext()
        self.head.setprev(None)
        return "sucessfully"

    def deletefromlast(self):
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.getprev()
            self.tail.setnext(None)
        return "sucesfully"

    def deleteatposition(self, pos):
        current = self.head
        if pos == 0:
            raise Exception("Please enter correct position")
        elif pos == 1:
            return self.deletefromstart()
        else:
            while current == pos - 1:
                current = current.getnext()

            # newnode.setnext(current.getnext())
            # newnode.setprev(current.getprev())
            # current.setnext(newnode)
            # current.getnext().setprev(newnode)
            return "sucessfully"


obj1 = DoublyLinkedlist()
obj1.insertatfirst(3)
obj1.insertatlast(6)
obj1.insertatlast(8)
obj1.insertatlast(17)
obj1.insertatfirst(9)
obj1.insertatposition(4, 2)
print(obj1.displaydata())
obj1.deletefromstart()
obj1.deletefromlast()
print(obj1.displaydata())