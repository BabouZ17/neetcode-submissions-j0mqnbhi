import heapq

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list) # userId: List[(count, TweetId)]
        self.followers = defaultdict(set) # userId: Set[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, heap = [], []

        self.followers[userId].add(userId)
        for followeeId in self.followers[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                heap.append([count, tweetId, followeeId, index - 1])

        heapq.heapify(heap)
        while heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(heap, [count, tweetId, followeeId, index - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)        
