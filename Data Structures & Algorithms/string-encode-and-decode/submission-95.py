class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=i
            s+="||"
        return s


    def decode(self, s: str) -> List[str]:
        k=[]
        p=""
        i=0
        while i< len(s):
            
            if s[i:i + 2] == "||":
                k.append(p)
                p=""
                i+=2

            else:
                p+=s[i]
                i+=1

        return k



        
        
