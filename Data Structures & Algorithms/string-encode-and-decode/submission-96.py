class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ''
        for i in strs:
            e+=i
            e+="||"
        return e


    def decode(self, s: str) -> List[str]:
        k=[]
        p=""
        i=0
        while i< len(s):
            if s[i:i+2]=="||":
                k.append(p)
                p=""
                i+=2
            else:
                p+=s[i]
                i+=1
        
        return k
