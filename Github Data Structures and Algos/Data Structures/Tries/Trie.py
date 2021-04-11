class node():
    def __init__(self, val):
        self.value = val
        self.children = [None for i in range(26)]
        self.isEnd = False

    def __repr__(self):
        return str(self.value)


class trie:
    def __init__(self):
        self.head = node(None)

    def __contains__(self, word):

        cur = self.head
        for i in range(len(word)):
            # since node children array is in ASCII order, we find the index of the char
            index = ord(word[i]) - ord("a")
            # we are looking for by using this expression

            # if a child at the given index is False we know that the word has not been added to the trie
            if cur.children[index] == None:
                return False

            # if the value of the child node at the given index matches the currect char, we see if it is the last char in the string
            if cur.children[index].value == word[i]:
                # if True we return True
                if i == len(word) - 1 and cur.children[index].isEnd == True:
                    return True

                else:  # else we continue the loop and we update cur
                    cur = cur.children[index]

            else:  # if none of these expressions return True, the word has not been added to the trie, or the current node is not defined.
                return False

    def add(self, word):
        # we start at the head and place the first char in the correct index
        cur = self.head
        for i in range(len(word)):
            # expression for finding right index of child node
            index = ord(word[i]) - ord("a")
            if cur.children[index] == None:  # if the index is none we create a new node
                newnode = node(word[i])
                cur.children[index] = newnode
                cur = newnode
                if i == len(word) - 1:
                    newnode.isEnd = True
            else:
                if i == len(word) - 1:
                    cur.children[index].isEnd = True
                else:
                    cur = cur.children[index]


t = trie()
t.add("hello")
t.add("hel")
print("helloo" in t)
print("hello" in t)
print("hel" in t)
