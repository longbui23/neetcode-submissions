class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = defaultdict(int)

        need_cnt, have_cnt = len(need), 0
        start = 0
        res_len, res = float('inf'), ""

        for end, char in enumerate(s):
            have[char] += 1

            if char in need and have[char] == need[char]:
                have_cnt += 1

            while have_cnt == need_cnt:
                if end - start + 1 < res_len:
                    res_len = end - start + 1
                    res = s[start:end + 1]
                
                have[s[start]] -= 1
                if s[start] in need and have[s[start]] < need[s[start]]:
                    have_cnt -= 1

                start += 1

        return res