#lc-227-basic calculator

class Solution:
    def calculate(self, s: str) -> int:

        s=s.replace(" ", "")
        stack=[]
        num=0
        pre_sign="+"
        n=len(s)

        for i in range(n):
            char=s[i]
            #if char is a number
            if char.isdigit():
                num=num*10 + int(char)
            #if char is sign
            if not char.isdigit() or i==n-1: #n-1 --> last one
                if pre_sign=="+":
                    stack.append(num)
                elif pre_sign=="-":
                    stack.append(-num)
                elif pre_sign=="*":
                    top=stack.pop()
                    multi=top*num
                    stack.append(multi)
                elif pre_sign=="/":
                    top=stack.pop()
                    divide=int(top/num) 
                    stack.append(divide)

                pre_sign=char
                num=0

        return sum(stack)

    



                








