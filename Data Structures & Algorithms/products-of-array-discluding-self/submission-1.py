class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        number=1
        number_list=[1]*len(nums)
        for i in range(1, len(nums)):
            number*=nums[i-1]
            number_list[i]=number
        number=1
        for i in reversed(range(0, len(nums)-1)):
            number*=nums[i+1]
            number_list[i]*=number
        

        return number_list
        