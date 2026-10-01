class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.visited = set()
        self.queue = []
        self.total = 1

        def compare(word1, word2):
            if len(word1) != len(word2):
                return 0
            total = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    total += 1
            return total

        def explore():
            while self.queue:
                size = len(self.queue)
                for i in range(size):
                    curr = self.queue.pop(0)
                    print(curr)
                    if curr == endWord:
                        return True
                    if curr in self.visited:
                        continue
                    self.visited.add(curr)
                    for wor in wordList:
                        if compare(curr, wor) == 1 and wor not in self.visited:
                            self.queue.append(wor)
                self.total += 1
        
        self.queue.append(beginWord)
        if explore():
            return self.total
        return 0