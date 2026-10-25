class Solution:

    def encode(self, strs: List[str]) -> str:
        chunks = []
        for s in strs:
            chunks.append(str(len(s)) + '#' + s)
        res = "".join(chunks)
        return res

    def decode(self, s: str) -> List[str]:
        res = []; i = 0

        while i<len(s):
            j=i
            length=0
            while s[j].isdigit():
                length=length*10+int(s[j])
                j+=1
            res.append(s[j+1:j+1+length])
            i=j+1+length
        
        return res
