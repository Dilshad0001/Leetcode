
# <---length of last word---->


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        length = 0
        for char in reversed(s):
            if char == ' ':
                
                break
            length += 1
        
        return length
