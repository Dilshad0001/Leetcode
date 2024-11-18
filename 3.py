class Solution:
    def reverse(self, x: int) -> int:
        if x==0 :
            return 0 
        flag=0
        k=0
        num=[]
        if x<0:
            flag=1
            x=x*-1
        num_list=list(str(x))
        num_list.reverse()
        for i in num_list:
            if int(i)>=1:
                k=1
            if k==1:
                num.append(i)
        num_result=int("".join(num))
        if num_result >=2147483647:
            return 0
        if flag==1:
            num_result=num_result*-1
        return num_result            





