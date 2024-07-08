# def searchRange(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     n=nums.count(target)
#     if len(nums)==0 or n==0:
#         return [-1,-1]
#     m=nums.index(target)
#     return [m,m+n-1]

# without using library function-------
def BinarySearch(nums,left,right,target):
    while left<=right:
        mid=int((left+right)/2)
        if nums[mid]==target:return mid
        elif nums[mid]>target:right=mid-1
        elif nums[mid]<target:left=mid+1
    return -1

def searchRange(nums,target):
    if len(nums)==0:return [-1,-1]
    start=BinarySearch(nums,0,len(nums)-1,target)
    if start==-1: return [-1,-1]
    end=start
    temp1=0
    temp2=0
    while start!=-1:
        temp1=start
        start=BinarySearch(nums,0,start-1,target)
    while end!=-1:
        temp2=end
        end=BinarySearch(nums,end+1,len(nums)-1,target)
    start=temp1
    end=temp2
    return [start,end]
# arr=[5,7,7,8,8,10]
# print(arr.count(6))
print(searchRange([5,7,7,8,8,10],7))
