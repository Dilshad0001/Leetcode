# Reverse Words in a String


class Solution:
    def reverseWords(self, s: str) -> str:
        j=[]
        m=s.split(" ")
        m.reverse()
        for i in m:
            if i !="":
                j.append(i)
                j.append(" ")
        k="".join(j) 
        res=k.strip()
        return res