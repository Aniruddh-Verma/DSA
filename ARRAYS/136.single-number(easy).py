class Solution:
    #find the number of occuring odd number of times  
    def singleNumber(self, nums: List[int],) -> int:
        res = 0
        for i in nums :
             res^= i
        
        return res
            
        