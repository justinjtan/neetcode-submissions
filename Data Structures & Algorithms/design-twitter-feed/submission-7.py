class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follow_list = defaultdict(list)
        self.recent_id = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.recent_id))
        self.recent_id += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        top_tweets = [] # min heap
        for tweet, pq in self.tweets[userId]:
            heapq.heappush(top_tweets, (pq, tweet))
            if len(top_tweets) > 10:
                heapq.heappop(top_tweets)
        for followee in self.follow_list[userId]:
            for followee_tweet, pq in self.tweets[followee]:
                heapq.heappush(top_tweets, (pq, followee_tweet))
                if len(top_tweets) > 10:
                    heapq.heappop(top_tweets)
        max_heap = [(-pq, tweet) for pq, tweet in top_tweets]
        heapq.heapify(max_heap)
        res = []
        for i in range(len(max_heap)):
            pq, tweet = heapq.heappop(max_heap)
            res.append(tweet)
        return res
        #WCRT: O(N) | Space: O(1)

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_list[followerId]:
            self.follow_list[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        for i in range(len(self.follow_list[followerId])):
            if self.follow_list[followerId][i] == followeeId:
                self.follow_list[followerId].pop(i)
                return
