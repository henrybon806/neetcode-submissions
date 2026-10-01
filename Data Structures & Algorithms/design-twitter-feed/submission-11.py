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
                tweet = self.tweets[person][-1]
                feed.append((tweet[0], tweet[1], tweet[2], len(self.tweets[person])-1))
        heapq.heapify(feed)
        output = []
        while feed and len(output) < 10:
            tweet = heapq.heappop(feed)
            output.append(tweet[2])
            if tweet[3] > 0:
                newtweet = self.tweets[tweet[1]][tweet[3]-1]
                heapq.heappush(feed, (newtweet[0], newtweet[1], newtweet[2], tweet[3]-1))
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.userDict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userDict[followerId].discard(followeeId)
        
