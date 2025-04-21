class RobotSorter:
    def __init__(self, robots):
        self.robots = robots

    def merge_sort(self):
        self.robots = self._merge_sort(self.robots)

    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self._merge_sort(arr[:mid])
        right = self._merge_sort(arr[mid:])
        
        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                result.append(left[i])
                i += 1
            elif left[i][0] > right[j][0]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def get_sorted_robots(self):
        return self.robots


N = int(input())
robots = []

for _ in range(N):
    main, aux = map(int, input().split())
    robots.append((main, aux))

robot_sorter = RobotSorter(robots)
robot_sorter.merge_sort()

sorted_robots = robot_sorter.get_sorted_robots()
for robot in sorted_robots:
    print(robot[0], robot[1])