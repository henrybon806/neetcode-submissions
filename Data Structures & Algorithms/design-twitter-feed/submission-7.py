class Twitter:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        self.queue = deque()
        self.time = 0
        self.tweets = defaultdict(list)
        self.userDict = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # heapq.heappush(self.heap, (self.time, userId, tweetId))
        self.tweets[userId].append((self.time, userId, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        people = self.userDict[userId] | {userId}
        for person in people:
            if self.tweets[person]:
                for tweet in self.tweets[person]:
                    feed.append(tweet)
        heapq.heapify(feed)
        count = min(10, len(feed))
        output = []
        for i in range(count):
            output.append(heapq.heappop(feed)[2])
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.userDict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userDict[followerId].discard(followeeId)
        
