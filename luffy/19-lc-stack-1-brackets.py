#lc-20-valid0-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={")":"(","]":"[","}":"{"}
        for char in s:
            if char in {"(","[","{"}:
                stack.append(char)
            else:
                if stack==[]: #if not stack:
                    return False


                top_ele=stack.pop()
                if mapping[char]!=top_ele:
                    return False


        if stack:
            return False
        else:
            return True




        

