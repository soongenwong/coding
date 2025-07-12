class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_counts = Counter(t)

        required = len(t_counts)

        left, right = 0, 0

        window_counts = {}

        formed = 0

        min_len = float('inf')
        ans_start_idx = 0

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in t_counts and window_counts[char] == t_counts[char]:
                formed += 1

            while formed == required and left <= right:
                current_window_len = right - left + 1
                if current_window_len < min_len:
                    min_len = current_window_len
                    ans_start_idx = left

                char_to_remove = s[left]
                window_counts[char_to_remove] -= 1

                if char_to_remove in t_counts and window_counts[char_to_remove] < t_counts[char_to_remove]:
                    formed -= 1

                left += 1

            right += 1

        if min_len == float('inf'):
            return ""

        else:
            return s[ans_start_idx : ans_start_idx + min_len]

#