
# unique path

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        k=m+n-2
        p=n-1
        h=m-1
        f_k=1
        f_p=1
        f_h=1
        for i in range(1,k+1):
            f_k=(f_k)*i
        for j in range(1,p+1):
            f_p=(f_p)*j  
        for r in range(1,h+1):
            f_h=(f_h)*r
        resul_t=(f_k)/(f_p*f_h)
        result=int(resul_t)
        return result            
