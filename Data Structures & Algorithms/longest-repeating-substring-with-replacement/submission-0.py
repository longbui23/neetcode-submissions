class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hsh = defaultdict(int)
        start = 0
        max_char = 0
        max_len = 0

        for end in range(len(s)):
            hsh[s[end]] += 1
            max_char = max(max_char, hsh[s[end]])

            while (end - start + 1) - max_char > k:
                hsh[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len