class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        lst = self.data[key]
        left, right = 0, len(lst) - 1
        lastVal = [-1, ""]
        while left <= right:
            middle = (left + right) // 2
            if lst[middle][0] == timestamp:
                return lst[middle][1]
            elif lst[middle][0] > timestamp:
                right = middle - 1
            else:
                if lst[middle][0] > lastVal[0]:
                    lastVal = [lst[middle][0], lst[middle][1]]
                left = middle + 1
        return lastVal[1]
        #WCRT: O(log N) | Space; O(1)