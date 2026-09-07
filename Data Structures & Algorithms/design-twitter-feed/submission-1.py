class Twitter:

    def __init__(self):
        self.tweet = [] # stores tweet id and user that posted it (tweetId, userId)
        self.table = {} # key is folowee, value is follower
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.table:
            self.table[userId] = set()
        self.tweet.append((tweetId, userId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        k = 0
        i = len(self.tweet) - 1
        while k < 10 and i >= 0:
            if userId in self.table and (self.tweet[i][1] in self.table[userId] or self.tweet[i][1] == userId):
                res.append(self.tweet[i][0])
                k += 1
            i -= 1
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.table:
            self.table[followerId] = set()
        self.table.get(followerId).add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.table:
            if followeeId in self.table[followerId]:
                self.table.get(followerId).remove(followeeId)
        
