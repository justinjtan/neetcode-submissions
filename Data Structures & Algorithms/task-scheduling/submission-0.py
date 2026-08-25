class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = ""
        char_count = defaultdict(int)
        for char in tasks:
            char_count[char] += 1
        max_heap = [[-ct, char] for char, ct in char_count.items()]
        heapq.heapify(max_heap)
        chars = []
        while max_heap:
            for i in range(n + 1):
                if max_heap:
                    char = heapq.heappop(max_heap)
                    res += char[1]
                    char[0] = char[0] + 1
                    if char[0] == 0:
                        continue
                    chars.append(char)
                elif chars:
                    res += "-" * ((n + 1) - i)
                    break
            while chars:
                heapq.heappush(max_heap, chars.pop())
        return len(res)
        #WCRT: O(N) | Space: O(1)
