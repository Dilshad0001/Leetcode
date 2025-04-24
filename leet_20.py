
class Solution:
    def isValid(self):
        s ="([])"                      
        r=[]
        m=[]
        for i in s:
            if i in "{([":
                r.append(i)
            elif r and ((i == ")" and r[-1] == "(") or
                        (i == "]" and r[-1] == "[") or
                        (i == "}" and r[-1] == "{")):
                r.pop()
        if len(r)==0:
            return True
        else:
            return False            


k=Solution()
print(k.isValid())



