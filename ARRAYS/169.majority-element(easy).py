class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=0
        count=1
        n=len(nums)
        for i in range(n):
            if nums[i]==m:
                count+=1
            else:
                count-=1
            if count==0:
                m=nums[i]
                count+=1
        count= 0
        for i in range(n):
            if nums[i]==m:
                count+=1
            if count>n/2:
                return m
                