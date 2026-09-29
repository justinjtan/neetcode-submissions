class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort()
        res = 0
        while cars:
            car_pos, car_speed = cars.pop()
            time_to_target = (target - car_pos) / car_speed
            while cars and time_to_target >= (target - cars[-1][0]) / cars[-1][1]:
                cars.pop()
            res += 1
        return res
        #WCRT: O(N log N) | Space: O(N)