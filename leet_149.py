class Solution:
    def most_repeat(self,m:list[float]):
        max_count=0
        max_repeat_element=m[0]
        for x in m:
            count=0
            for h in m:
                if x==h:
                    count=count+1
            if max_count<count:
                max_count=count
                max_repeat_element=x  
        if max_count==1:
            x,y,z=m[0]
            return 999999-x-x**2       
        return max_repeat_element              
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==1 or len(points)==0:
            return len(points)
        slope_list=[]
        for i in points:
            sl_list=[]
            x1,y1=i
            for j in points:
                if i!=j:
                    x2,y2=j
                    if x2-x1!=0:
                        slope=(y2-y1)/(x2-x1)
                        x_co=0
                        y_co=round(y1-(slope*x1),2)
                    else:
                        slope=float('inf')
                        x_co=x1
                        y_co=0
                    sl_list.append([slope,x_co,y_co])            
            r=self.most_repeat(sl_list)
            slope_list.append(r)
        d=self.most_repeat(slope_list)
        return slope_list.count(d)            



        