class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hsh = defaultdict(int)
        start = 0
        max_len = 0

        for end in range(len(s)):
            if s[end] in hsh:
                start = max(start, hsh[s[end]])
            hsh[s[end]] = end + 1
            max_len = max(max_len, end - start + 1)

        return max_len

