class WordDictionary:

    def __init__(self):
        self.graph = {}
        self.root = {}
        self.maxlen = 0

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return "$" in node
            ch = word[i]
            if ch == ".":
                return any(dfs(i + 1, child) for key, child in node.items() if key != "$")
            return ch in node and dfs(i + 1, node[ch])

        return dfs(0, self.root)
