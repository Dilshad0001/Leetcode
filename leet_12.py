# Integer to Roman



class Solution:
    def intToRoman(self, num: int) -> str:
        k=int(num/1000)
        k_r=num-(k*1000)
        if k_r<900:
            f=int(k_r/500)
            f_r=k_r-(f*500)
        else:
            f=0
            f_r=k_r    
        h=int(f_r/100)
        h_r=f_r-(h*100)
        if h_r<90:
            fi=int(h_r/50)
            fi_r=h_r-(fi*50)
        else:
            fi=0
            fi_r=h_r    
        t=int(fi_r/10)
        t_r=fi_r-t*10
        if t_r<9:
            fiv=int(t_r/5)
            fiv_r=t_r-(fiv*5)
        else:
            fiv=0
            fiv_r=t_r    
        one=fiv_r



        lis=[]
        for m in range(k):
            lis.append("M")
        for n in range(f):
            lis.append("D")
        if h==4:
            lis.append("CD")
        elif h==9:
            lis.append("CM") 
        else:       
            for p in range(h):
                lis.append("C")
        for q in range(fi):
            lis.append("L")
        if t==4:
            lis.append("XL")
        elif t==9:
            lis.append("XC")
        else:
            for u in range(t):
                lis.append("X")
        for v in range(fiv):
            lis.append("V")
        if one==4:
            lis.append("IV")
        elif one==9:
            lis.append("IX")
        else:
            for w in range(one):
                lis.append("I")       



        result="".join(lis)
        return result             



        