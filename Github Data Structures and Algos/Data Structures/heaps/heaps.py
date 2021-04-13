from math import floor
class heap(object):

    def __init__(self):
        self.data = []
    
    def isempty(self):
        return len(self.data) == 0
    
    def getleft(self, i):
        result = 2*i+1 
        if result > len(self.data)-1:
            return -1
        else:
            return result

    def getright(self, i):
        result = 2*i+2
        if result > len(self.data)-1:
            return -1
        else:
            return result
        
    def hasright(self, i):
        if i*2 + 2 < len(self.data):
            return True
        else:
            return False

    def hasleft(self, i):
        if i*2 + 1 < len(self.data):
            return True
        else:
            return False

    def getparent(self, i):
        return int((i-1)/2)
    def hasparent(self, i):
        return self.getparent(i) >=0
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def heapup(self, i):
        while (self.data[i] > self.data[self.getparent(i)]) and self.hasparent(i):
            self.swap(i, self.getparent(i))
            i = self.getparent(i)
        
    def insert(self, data):
        self.data.append(data)
        self.heapup(len(self.data)-1)
    
    def isvalidparent(self, i):

        if not self.hasleft(i):
            return True
        elif not self.hasright(i):
            return self.data[i] > self.data[self.getright(i)]
        else:
            return (self.data[i] > self.data[self.getright(i)] and self.data[i] > self.data[self.getleft(i)])

    def remove(self):
        if len(self.data) == 0:
            print("error")

        root = self.data[0]
        
        self.data[0] = self.data[-1]
        self.data.pop(-1)
        i = 0
        while not self.isvalidparent(i):
            greaterchild = None 
            if self.data[self.getright(i)] > self.data[self.getleft(i)]:
                greaterchild = self.getright(i)
            elif self.data[self.getleft(i)] >= self.data[self.getright(i)]:
                greaterchild = self.getleft(i)

            self.swap(i, greaterchild)
            i = greaterchild
        
        return root


def kthlargestitem(array, k):
    if len(array) == 0:
        pass
    else:
        hea = heap()
        for item in array:
            hea.insert(item)

        for i in range(k-1):
            hea.remove()
        
        print(hea.remove())


kthlargestitem([1,2,3,4,6,7,8,9,10], 7)


