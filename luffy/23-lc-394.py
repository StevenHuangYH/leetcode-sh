#lc-394-decode-string
class Solution:
    def decodeString(self, s: str) -> str:
        # 初始化一个栈来保存之前读取的字符和重复次数，cur_num用来累积当前数字
        stack = []
        cur_num = 0
        
        for char in s:
            if char.isdigit():
                # 如果是数字，累加计算多位数值（例如，连续读到'1'和'2'会变成12）
                cur_num = cur_num * 10 + int(char)
                
            elif char == "[":
                # 遇到 '[' 代表前面的数字已经完整，把数字和 '[' 压入栈中保存状态
                stack.append(cur_num)
                cur_num = 0       # 重置 cur_num，以便记录嵌套在里面的下一个数字
                stack.append("[")
                
            elif char == "]":
                # 遇到 ']' 代表当前括号内的子串结束，开始处理
                sub_strs = []
                # 一直出栈，直到遇到与之匹配的 '[' 为止
                while stack[-1] != "[":
                    sub_strs.append(stack.pop())
                
                # 因为栈是后进先出，所以取出来的字符顺序是反的，需要反转一下
                sub_strs.reverse()
                inner_strs = "".join(sub_strs) # 组合成正确的括号内字符串
                
                stack.pop() # 弹出栈顶的 '['
                
                # 弹出对应的重复次数（在压入 '[' 前压入的那个数字）
                repeat_time = stack.pop()
                
                # 将括号内的字符串复制对应的次数，并作为一个整体重新压入栈中
                stack.append(inner_strs * repeat_time)
                
            else: 
                # 如果是普通的英文字母，直接压入栈中
                stack.append(char)
                
        # 遍历结束后，栈中只剩下解码后的字符串片段，将它们拼接成最终结果返回
        return "".join(stack)


#  O(n)


        

