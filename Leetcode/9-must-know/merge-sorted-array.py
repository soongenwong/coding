class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        midx = m - 1
        nidx = n - 1 
        right = m + n - 1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1

            right -= 1
        

        # intial plan
        # use hashmap to store values
        # merge values together
        # sort values from small to large

        # final solution
        # start from the end because there might be zero behind. 
        # find the index of the merged solution. 
        # loop continues as long as nums2 has values
        # look for the larger value, place it on the right, then decrement it. 
        # start from the back so you only overwrite the unsued space in nums1