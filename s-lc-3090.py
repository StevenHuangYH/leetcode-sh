# 3090. Maximum Length Substring With Two Occurrences
# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/



class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        right=0
        left=0
        counts={}
        max_len=0

        while right < len(s):
            if counts.get(s[right],0) == 2:
                counts[s[left]] -= 1
                left +=1 

            else:
                counts[s[right]] = counts.get(s[right], 0) + 1
                max_len=max(max_len, right - left + 1)
                right += 1

        return max_len

        


        #.get()
        #