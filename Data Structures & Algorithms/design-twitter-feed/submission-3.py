class Twitter:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        self.queue = deque()
        self.time = 0
        self.userDict = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.heap, (self.time, userId, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        count = 10
        items = []
        while count > 0:
            if not self.heap:
                break
            item = heapq.heappop(self.heap)
            if item[1] == userId or (userId in self.userDict and item[1] in self.userDict[userId]):
                feed.append(item[2])
                count -= 1
            items.append(item)
        for item in items:
            heapq.heappush(self.heap, item)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userDict:
            self.userDict[followerId] = [followeeId]
            return
        if followeeId not in self.userDict[followerId]:
            self.userDict[followerId] = self.userDict[followerId] + [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId  in self.userDict[followerId]:
            self.userDict[followerId].remove(followeeId)
        
