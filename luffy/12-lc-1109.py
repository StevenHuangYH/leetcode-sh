#lc-1109
#corporate flight bookings

from typing import List

#[0]*n -> create a list with n elements, each element is 0

class Solution: #general way: worst case
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * n
        for first, last, seats in bookings:
            for i in range(first-1, last):
                answer[i] += seats

        return answer

#large range modify 
#use difference array

class Solution2:  #difference array
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0]*(n+1)
        for first, last, seats in bookings:
            diff[first-1]+=seats
            diff[last]-=seats
        
        answer =[0]*n
        last_Seats = 0 
        for i in range(n):
            answer[i]=last_Seats + diff[i]
            last_Seats = answer[i]
        return answer


        







        

