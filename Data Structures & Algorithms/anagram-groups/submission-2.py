from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prefix_dict=defaultdict(list)
        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c)-ord("a")]+=1

            count_key = tuple(count)
            prefix_dict[count_key].append(s)
        
        return list(prefix_dict.values())
        