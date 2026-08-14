from typing import List


#try sliding window 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right =0
        my_set = set()
        max_len = 0
        while right < len(s):
            if s[right] in my_set: #if the set has recorded
                my_set.remove(s[left])
                left += 1
            else: # if the current character is not in the set
                my_set.add(s[right])
                max_len = max(max_len, right-left+1)
                right += 1

        return max_len
    
    
                