class Node:
    def __init__(self, data=None, next=None):
        # self.length = 0
        self.data = data
        self.next = next

    def setdata(self, data):
        self.data = data

    def getdata(self):
        return self.data

    def setnext(self, next):
        self.next = next

    def getnext(self):
        return self.next

    # def set_len(self, length):
    #     self.length = length
    #
    # def get_len(self):
    #     return self.length


class LinkedList:
    len = len

    def __init__(self, head=None):
        self.head = head

    def insertatstart(self, data):
        newnode = Node()
        newnode.setdata(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.setnext(self.head)
            self.head = newnode
        return self.head.data

    def display_data(self):
        current = self.head
        count = 0
        while current:
            print(current.data)
            count = count + 1
            current = current.getnext()
        return "Count:-", count

    def insertatend(self, data):
        newnode = Node()
        newnode.setdata(data)
        current = self.head
        while current.getnext() is not None:
            current = current.getnext()
        current.setnext(newnode)
        return

    def insertatpos(self, data, pos):
        newnode = Node()
        newnode.setdata(data)
        if pos == 0:
            raise ValueError("Please enter correct position")
        elif pos == 1:
            return self.insertatstart(data)
        else:
            current = self.head
            while current is pos - 1:
                current = current.getnext()
            newnode.setnext(current.getnext())
            current.setnext(newnode)
        return "sucessfully"

    def deletefromfirst(self):
        if self.head is None:
            raise ValueError("Please enter correct position")
        else:
            self.head = self.head.getnext()
        return "suceesfully deleted"

    def deletefromlast(self):
        if self.head is None:
            raise ValueError("There is no element to remove")
        current = self.head
        previous = self.head
        if current.getnext() is None:
            self.head = None
        else:
            while current.getnext() is not None:
                previous = current
                current = current.getnext()
            previous.setnext(None)
        return "sucessfully"

    def deletefrompos(self, pos):
        if pos == 0:
            raise ValueError("Please enter correct position")
        elif pos == 1:
            return self.deletefromfirst()
        current = self.head
        previous = self.head
        count = 0
        while current.getnext() is not None:
            count = count + 1
            if count == pos:
                previous.setnext(current.getnext())
                return
            else:
                previous = current
                current = current.getnext()

    def deletefromdata(self, data):
        current = self.head
        previous = self.head
        flag = False
        while current.getnext() is not None:
            if current.data == data:
                flag = True
                previous.setnext(current.getnext())
                return
            else:
                previous = current
                current = current.getnext()
        if not flag:
            raise Exception("{} is not present in linkedlist".format(data))


obj1 = LinkedList()
obj1.insertatstart(3)
obj1.insertatstart(4)
obj1.insertatend(7)
obj1.insertatend(8)
obj1.insertatpos(2, 2)
obj1.insertatpos(9, 1)
print(obj1.display_data())
obj1.deletefrompos(3)
obj1.deletefromdata(10)
print(obj1.display_data())
