from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # fetch tweets from user
        feed = list(self.tweets[userId])
        for followee in self.followers[userId]:
            feed.extend(self.tweets[followee])

        heapq.heapify(feed)
        res = list()
        while feed and len(res) < 10:
            _, tweet = heapq.heappop(feed)
            res.append(tweet)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
