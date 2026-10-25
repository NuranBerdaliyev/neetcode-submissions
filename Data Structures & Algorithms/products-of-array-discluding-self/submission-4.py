class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        number=1
        prefix_number_list=[1]*len(nums)
        suffix_number_list=[1]*len(nums)
        for i in range(1, len(nums)):
            number*=nums[i-1]
            prefix_number_list[i]=number
        number=1
        for i in reversed(range(0, len(nums)-1)):
            number*=nums[i+1]
            suffix_number_list[i]=number
        number_list=[]
        for i, num in enumerate(nums):
            product=prefix_number_list[i]*suffix_number_list[i]
            number_list.append(product)

        return number_list
        