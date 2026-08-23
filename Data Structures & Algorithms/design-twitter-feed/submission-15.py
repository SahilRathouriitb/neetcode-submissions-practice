class Twitter:

    def __init__(self):
        self.tweet_count = 0
        self.user_map = {}
        self.followers = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_count += 1
        if userId in self.user_map:
            self.user_map[userId][0].add((tweetId, self.tweet_count))
            self.user_map[userId][1].add((tweetId, self.tweet_count))
        else:
            self.user_map[userId] = [{(tweetId, self.tweet_count)},{(tweetId, self.tweet_count)}]  
        
        if userId in self.followers:
            for i in self.followers[userId]:
                self.user_map[i][1].add((tweetId,self.tweet_count))
        


    def getNewsFeed(self, userId: int) -> List[int]:
        set_feed = self.user_map[userId][1]
        b = sorted(set_feed, key = lambda x: x[1], reverse = True)
        k = [i[0] for i in b]
        if len(k) > 10:
            return k[0:10]
        return k
        
        

    def follow(self, followerId: int, followeeId: int) -> None: 
        if followeeId not in self.followers:
            self.followers[followeeId] = {followerId}
        else:
            self.followers[followeeId].add(followerId)

        if followeeId not in self.user_map:
            self.user_map[followeeId] = [set(),set()]
        if followerId not in self.user_map:
            self.user_map[followerId] = [set(),set()]

        check_posts = self.user_map[followeeId][0]
        
        for i in check_posts:
            self.user_map[followerId][1].add(i)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followeeId in self.followers and followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)

            check_posts = self.user_map[followeeId][0]
            for i in check_posts:
                    self.user_map[followerId][1].remove(i)
        
