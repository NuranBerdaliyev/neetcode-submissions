class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        number=1
        prefix_list=[]
        for num in nums:
            prefix_list.append(number)
            number*=num
            
        number=1
        suffix_list=[]
        for num in reversed(nums):
            suffix_list.append(number)
            number*=num

        suffix_list.reverse()
        nums=[]
        for left, right in zip(prefix_list, suffix_list):
            nums.append(left*right)
        
        return nums

        