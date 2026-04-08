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
        res = []

        feed = self.tweets[userId][:]
        for followeeId in self.followers[userId]:
            feed.extend(self.tweets[followeeId])

        heapq.heapify(feed)
        while feed and len(res) < 10:
            _, tweetId = heapq.heappop(feed)
            res.append(tweetId)
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)        
