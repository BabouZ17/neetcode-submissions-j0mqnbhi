import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) # userId: List[(time, TweetId)]
        self.followers = defaultdict(set) # userId: Set[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # fetch user tweets
        feed = self.tweets[userId][:]

        # fetch tweets from other users being followed by userId
        for follower in self.followers[userId]:
            feed.extend(self.tweets[follower])

        feed.sort(key=lambda x: -x[0])
        return [tweet for _, tweet in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)        
