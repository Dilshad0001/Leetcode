class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            ind=nums.index(target)
            return ind
        else:
            large=[x for x in nums if x>target]
            large.sort()
            if large==[]:
                ind=len(nums)
                return ind
            small=[x for x in nums if x<target]
            small.sort(reverse=True)
            if small==[]:
                ind=0
                return ind
            ind=nums.index(large[0])
            return ind       
            
           


