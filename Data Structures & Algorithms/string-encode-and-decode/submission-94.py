class Solution:

    def encode(self, strs: List[str]) -> str:
        # k= "".join(strs)
        # s=""
        # if " " not in k:
        #     for i in strs:
        #         s+=i
        #         s+="|"
        #     return s
        # else:
        #     for i in strs:
        #         s+=i
        #         s+="|"
        #     return s
        s=""
        for i in strs:
            s+=i
            s+="||"
        return s
        # return strs


    def decode(self, s: str) -> List[str]:
        # l=[]
        # for i in s:
        #     l.append(i)

        # l = "".join(l)
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
        # return s


        
        
