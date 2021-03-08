
class stack(list):
    def __init__(self):
        super().__init__()

    def push(self, v):
        self.insert(0, v)

    def popleft(self):
        try:
            return self.pop(0)
        except IndexError:
            return False

    def peek(self):
        try:
            return self[0]
        except IndexError:
            return False


charMatch = {"}": "{", ")": "(", "]": "["}


def bracketVerify(string):
    s = stack()
    for char in string:
        if char in ["(", "{", "["]:
            s.push(char)
        elif char in ["}", "]", ")"]:
            if charMatch[char] == s.peek():
                s.popleft()

            else:
                return False
    if len(s) > 0:
        return False
    return True


for i in range(int(input())):
    if bracketVerify(input()):
        print("YES")
    else:
        print("NO")
