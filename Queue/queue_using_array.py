class queue(object):
    def __init__(self, limit=5):
        self.limit = limit
        self.rare = None
        self.front = None
        self.que = []
        self.size = 0

    def isEmpty(self):
        return "Queue is Empty"

    def enqueue(self, item):
        if self.size >= self.limit:
            self.resize()
        self.que.append(item)
        if self.front is None and self.rare is None:
            self.rare = self.front = 0
        else:
            self.rare = self.size

        self.size = self.size + 1

    def dequeue(self):
        if self.size <= 0:
            return "Queue is Empty"
        else:
            self.front.pop(0)
            self.size = self.size - 1
            if self.size == 0:
                self.front = self.rare = None
            else:
                self.rare = self.size - 1

    def resize(self):
        newqueue = self.que
        self.limit = 2 * self.limit
        self.que = newqueue

    def queuerare(self):
        if self.rare is None:
            raise IndexError
        else:
            return self.que[self.rare]

    def queuefront(self):
        if self.front is None:
            raise IndexError
        else:
            return self.que[self.front]


obj1=queue()
obj1.enqueue(2)
obj1.enqueue(4)
obj1.enqueue(47)
obj1.enqueue(8)
obj1.enqueue(54)
obj1.enqueue(49)
print(obj1.queuefront())
print(obj1.queuerare())
