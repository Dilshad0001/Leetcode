# def rotation_count(nums):
#     start=0                  
#     end=len(nums)-1          
#     while start<=end:
#         mid=(start+end)//2  
#         if nums[start]<nums[end]:     
#             return (start)    
#         elif nums[mid]<nums[start]:   
#             if nums[mid-1]>nums[mid]:
#                 return (mid)
#             end=mid-1
#         elif nums[mid]>nums[start]:   
#             if nums[mid+1]<nums[mid]:  
#                 return ( mid+1)        
#             start=mid+1


# target=1



# nums=[1]
# k=rotation_count(nums)
# print(k)
# res=nums[k:]+nums[:k]
# print(res)
         
# start=0
# end=len(res)-1
# while start<=end:
    
#     mid=(start+end)//2
#     if res[mid]==target:
#         print( type(mid))
#         break
#     elif res[mid]<target:
#         start=mid+1
#     else:
#         end=mid-1
# else:
#     print(-1)  
 

 


         


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return -1



























# def rotation_count(nums):
#     start=0                  #0
#     end=len(nums)-1          #6
#     while start<end:
#         mid=(start+end)//2  #3
#         # return mid
#         if nums[start]<nums[end]:     #4<2
#             return (start)    
#         elif nums[mid]<nums[start]:   #7<4
#             if nums[mid-1]>nums[mid]:
#                 return (mid)
#             end=mid-1
#         elif nums[mid]>nums[start]:   #7>4
#             if nums[mid+1]<nums[mid]:  #0<7
#                 return ( mid+1)        #4
#             start=mid+1



# nums=[4,5,6,7,0,1,2]
# k=rotation_count(nums)
# print(k)            
                    


        