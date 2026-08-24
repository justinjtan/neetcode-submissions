class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for i in range(len(points)):
            xi = points[i][0]
            yi = points[i][1]
            curr_distance = math.sqrt(pow(xi, 2) + pow(yi, 2))
            distance.append((curr_distance, i))
        min_heap = [(dis, i) for dis, i in distance]
        heapq.heapify(min_heap)
        res = []
        while k > 0:
            dis, points_idx = heapq.heappop(min_heap)
            res.append(points[points_idx])
            k -= 1
        return res
        #WCRT: O(N log k) | Space: O(k)