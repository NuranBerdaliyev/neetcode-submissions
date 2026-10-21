from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary_sex = defaultdict(int)
        for c in s:
            dictionary_sex[c]+=1
        for c in t:
            dictionary_sex[c] -= 1
        
        return not any(dictionary_sex.values())
        