'''
    Queue data structure by Saadkhalid913
'''


class Queue(list):
    def __init__(self):
        super().__init__()

    def push(self, i):
        self.append(i)

    def deque(self):
        return self.pop(0)

    def peek(self):
        return self[0]

    def isempty(self):
        return len(self) == 0


if __name__ == "__main__":
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q)
    print(q.deque())
    print(q)
