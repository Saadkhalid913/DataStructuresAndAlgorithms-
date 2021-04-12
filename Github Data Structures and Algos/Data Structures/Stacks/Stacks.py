'''
Stack data structure by Saadkhalid913

'''


class Stack(list):
    def __init__(self):
        super().__init__()

    def push(self, i):
        self.append(i)

    def isempty(self):
        return len(self) == 0

    def peek(self):
        return self[-1]


if __name__ == "__main__":
    q = Stack()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q)
    print(q.pop())
    print(q)
