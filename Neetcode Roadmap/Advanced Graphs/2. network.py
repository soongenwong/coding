class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1

        #Dijkstra's Algorithm
        #Time Complexity: O(E log V)
        #Space Complexity: O(E + V)
        #where E is the number of edges and V is the number of vertices
        #This is because we use a min heap to store the nodes to visit
        #and a set to store the nodes that have been visited
        #and a dictionary to store the edges