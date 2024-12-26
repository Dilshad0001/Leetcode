# <------Sqrt(x)------>



class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:  
            return 0
        
        left, right = 1, x  
        result = 0  
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid  
            elif mid * mid < x:
                result = mid  
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    


