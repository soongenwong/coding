class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        dist = [100000000] * n
        visit = [False] * n
        edges, res = 0, 0

        while edges < n - 1:
            visit[node] = True
            nextNode = -1
            for i in range(n):
                if visit[i]:
                    continue
                curDist = (abs(points[i][0] - points[node][0]) + 
                           abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
                    
            res += dist[nextNode]
            node = nextNode
            edges += 1

        return res

        #Prim's Algorithm
        #Time Complexity: O(n^2)
        #Space Complexity: O(n)
        #where n is the number of points
        #This is because we use a list to store the distances
        #and a list to store the visited points
        #and a list to store the edges
        #and a list to store the result