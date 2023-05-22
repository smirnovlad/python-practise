from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist = []
        lastPos = -1
        seats.append(1)
        for pos, val in enumerate(seats):
            if val:
                dist.append(pos - lastPos - 1)
                lastPos = pos
        ans = max(dist[0], dist[-1], (max(dist) + 1) // 2)
        return ans