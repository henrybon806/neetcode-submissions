class PrefixTree:

    def __init__(self):
        self.tree = {}
        

    def insert(self, word: str) -> None:
        node = self.tree
        for i, let in enumerate(word):
            if let not in node:
                # if i < len(word) -1:
                node[let] = {}
            node = node[let]
        node['*'] = True

    def search(self, word: str) -> bool:
        node = self.tree
        for i, let in enumerate(word):
            if let not in node:
                return False
            node = node[let]
        return '*' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.tree
        for i, let in enumerate(prefix):
            if let not in node:
                return False
            node = node[let]
        return True
        
        