class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        li=nums1+nums2
        li.sort()
        size=len(li)
        if size %2!=0:
            k=int(size/2)
            return float(li[k])
        else:
            k=(li[int(size/2)]+li[int((size/2)-1)])/2
            return float(k)  

        