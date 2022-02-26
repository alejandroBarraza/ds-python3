from NodeTree import NodeTree


class Trie:
    def __init__(self):
        self.root = NodeTree()

    def insert(self, word):
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c] = NodeTree()
            curr = curr.children[c]
        curr.idEnd = True

    def search(self, word):
        curr = self.root
        for c in word:
            if not c in curr.children:
                return False
            curr = curr.children[c]
        return curr.idEnd

    def start_with(self, word):
        curr = self.root
        for c in word:
            if not c in curr.children[c]:
                return False
            curr = curr.children[c]
        return True
