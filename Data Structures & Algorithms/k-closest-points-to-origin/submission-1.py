class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for i in range(len(points)):
            xi = points[i][0]
            yi = points[i][1]
            curr_distance = math.sqrt(pow(xi, 2) + pow(yi, 2))
            if len(distance) == k:
                heapq.heappushpop(distance, (-curr_distance, i))
            else:
                heapq.heappush(distance, (-curr_distance, i))
        res = []
        for dis, points_idx in distance:
            res.append(points[points_idx])
        return res
        #WCRT: O(N log k) | Space: O(k)