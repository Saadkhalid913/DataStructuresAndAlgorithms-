class PriorityQueue(list):
    def __init__(self):
        super().__init__()

    def push(self, a):
        for j in range(len(self)):
            if self[j] < a:
                self.insert(j, a)
                return

        self.append(a)

    def deque(self):
        return self.pop(0)

    def peek(self):
        return self[0]

    def isempty(self):
        return len(self) == 0


if __name__ == "__main__":
    p = PriorityQueue()
    p.push(1)
    p.push(2)
    p.push(3)
    print(p)
    p.pop()
    print(p)
