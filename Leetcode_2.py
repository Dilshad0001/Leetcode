# longest substring without repeating charecter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeat_li=[]
        size=[]
        for i in s:
            if i in repeat_li:
                size.append(len(repeat_li))
                inde=repeat_li.index(i)
                del repeat_li[:inde+1]
                repeat_li.append(i)
            else:
                repeat_li.append(i)
        else:
            size.append(len(repeat_li))        
        highest=max(size)
        return highest        