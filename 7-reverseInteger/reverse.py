class Solution:
    def reverse(self, x: int) -> int:
        # init res
        res = 0
        # init sign 
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            last_bit = x % 10
            res = res * 10 + last_bit
            
            # check the bondary 
            if res > 2**31 - 1:
                return 0
            elif res < -2**30:
                return 0 
            
            x //= 10
        
        return res * sign

