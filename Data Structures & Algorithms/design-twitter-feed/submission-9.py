class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follow_list = defaultdict(set)
        self.recent_id = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.recent_id))
        self.recent_id += 1
        #WCRT: O(1) | Space: O(1)

    def getNewsFeed(self, userId: int) -> List[int]:
        top_tweets = [] # min heap
        for tweet, pq in self.tweets[userId][-10:]:
            heapq.heappush(top_tweets, (pq, tweet))
        for followee in self.follow_list[userId]:
            for followee_tweet, pq in self.tweets[followee][-10:]:
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
        #WCRT: O(f) | Space: O(1) where f is the number of followee

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_list[followerId].add(followeeId)
        # Time: O(1) avg, O(N) worst case

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_list[followerId].discard(followeeId)
        # Time: O(1) avg, O(N) worst case
