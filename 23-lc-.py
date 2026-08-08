#lc-394-decode-string

class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        cur_num=0


        for char in s:
            if char.isdigit():
                cur_num=cur_num*10 + int(char)
            elif char=="[":
                stack.append(cur_num)
                cur_num=0
                stack.append("[")
            elif char=="]":
                # str=""
                # while stack[-1]!="[":
                #     str=stack.pop()+str
                sub_strs=[]
                while stack[-1]!="[":
                    sub_strs.append(stack.pop())

                sub_strs.reverse()
                inner_strs="".join(sub_strs)

                stack.pop()
                repeat_time= stack.pop()

                stack.append(inner_strs * repeat_time)

            else:#if char is letter
                stack.append(char)


        return "".join(stack)


#  O(n)


        

