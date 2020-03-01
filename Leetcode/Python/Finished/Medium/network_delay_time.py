import collections
import heapq

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        returns the longest path in the given graph, if none exists output -1
        :param times: Array of Array of ints
        :param N: Int
        :param K: Int
        :return: Int
        """
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        if len(dist) == N:
            return max(dist.values())
        else:
            return -1
