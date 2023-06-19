class stack(object):
    def __init__(self, limit=20):
        self.stk = []
        self.limit = limit

    def is_empty(self):
        return len(self.stk) <= 0

    def push(self, item):
        if len(self.stk) >= self.limit:
            return False
        else:
            self.stk.append(item)

    def pop(self):
        if len(self.stk) <= 0:
            print("stack underflow")
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            print("stack underflow")
            return 0
        else:
            return self.stk[-1]

    def size(self):
        return self.stk

    def print_element(self):
        for i in self.stk:
            print(i)

obj1 = stack()
obj1.push(3)
obj1.push(5)
obj1.push(6)
obj1.pop()
obj1.print_element()