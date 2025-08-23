class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mn = float('-inf')
        seen = set()
        sum_ = 0

        for val in nums:
            if val not in seen:
                # if element first occurured, hence unique
                if val >= 0:
                    sum_ += val
                else:
                    mn = max(mn, val)

            seen.add(val)

        if sum_ == 0 and 0 not in seen:
            return mn

        return sum_