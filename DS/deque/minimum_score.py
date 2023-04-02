"""You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.
"""

from collections import defaultdict
from deque_array_based import Deque

def min_score(n, roads) -> int:
        dict = defaultdict(list)
        for a,b,c in roads:
            dict[a].append([b,c])
            dict[b].append([a,c])
        seen = set()
        score = 1000000    
        q = Deque()
        q.enqueue_first(1)
        while q:
            node = q.dequeue_last()
            for a,b in dict[node]:
                score = min(score,b)
                if a not in seen:
                    q.enqueue_last(a)
                    seen.add(a)
        return score

if __name__ == "__main__":
    
    print(min_score(4,[[1,2,2],[1,3,4],[3,4,7]]))
    
    