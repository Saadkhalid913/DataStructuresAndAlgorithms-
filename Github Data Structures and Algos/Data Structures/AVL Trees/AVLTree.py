class AVLNode():
    def __init__(self, value=None):
        self.V = value
        self.R = None
        self.L = None

    def __repr__(self):
        return str(self.V)


class AVLTree():
    def __init__(self):
        self.head = None

    def GetNodeHeight(self, node: AVLNode):
        if node == None:
            return 0
        else:
            return 1 + max(self.GetNodeHeight(node.L), self.GetNodeHeight(node.R))

    def GetTreeHeight(self):
        return self.GetNodeHeight(self.head)

    def __insertRecursive(self, node: AVLNode, Value: int):
        if node == None:
            return AVLNode(Value)
        else:
            if Value > node.V:
                node.R = self.__insertRecursive(node.R, Value)
            else:
                node.L = self.__insertRecursive(node.L, Value)
        return node

    def insert(self, Value: int):
        if self.head == None:
            self.head = AVLNode(Value)

        else:
            self.head = self.__insertRecursive(self.head, Value)

    @property
    def BalanceFactor(self):
        return self.GetNodeHeight(self.head.L) - self.GetNodeHeight(self.head.R)

    @property
    def RightHeavy(self):
        return self.BalanceFactor < -1

    @property
    def LeftHeavy(self):
        return self.BalanceFactor > 1

    def IsLeftHeavy(self, node: AVLNode):
        return self.GetNodeHeight(node.R) - self.GetNodeHeight(node.L) < -1

    def IsRightHeavy(self, node: AVLNode):
        return self.GetNodeHeight(node.R) - self.GetNodeHeight(node.L) > 1

    def NodeBalanceFactor(self, node: AVLNode):
        return self.GetNodeHeight(node.L) - self.GetNodeHeight(node.R)

    def balance(self, node):
        if self.IsLeftHeavy(node):
            if self.NodeBalanceFactor(node.L) > 1:
                print("Right rotation on " + node.L.__str__())
            else:
                print("Left Rotation on " + node.L.__str__())
        else:
            if self.NodeBalanceFactor(node.R) > 1:
                print("Left rotation on " + node.R.__str__())
            else:
                print("Right rotation on " + node.R.__str__())


T = AVLTree()
T.insert(1)
T.insert(2)
T.insert(3)
print(T.NodeBalanceFactor(T.head.R))

pass
