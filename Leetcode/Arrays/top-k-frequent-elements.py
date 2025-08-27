class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res


        # initial plan
        # find the first value and look for duplicates. 
        # find how many times it is seen
        # identify the most frequent elements based on the required amount k

        # final solution
        # counts how many times each number appears in nums.
        # heapq is a min heap by default
        # push every pair into the heap, for max heap, so -val
        # pop the element with the highest frequency k times from the heap. 
        # heapq.heappop(heap) gets the number, [1] is to get 1 number 
        