#905. Sort Array By Parity

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0 
        j=n-1
        while i<j:
            if nums[i]%2 !=0:
                nums[i] , nums[j]=nums[j] , nums[i]
                j-=1
            else:
                i+=1
        return nums
        