class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prefix_dict: dict[int, list[int]] = {}
        for i in range(len(nums)):
            if target-nums[i] in prefix_dict:
                return [prefix_dict[target-nums[i]][0], i]
            count = prefix_dict.setdefault(nums[i], [])
            count.append(i)
        return []


            




        