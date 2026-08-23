from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cnt = Counter() #hashmap key: char; value: int
        left = 0
        for right, c in enumerate(s):
            cnt[c] += 1 #字符的出现次数+1
            while cnt[c]>1:
                cnt[s[left]] -= 1 # remove s[left] from the set 
                left += 1
            ans = max(ans, right - left + 1) #字符个数
        return ans
        