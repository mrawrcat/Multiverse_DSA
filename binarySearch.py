'''
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

Summary/Explanation:

A binary search attempts to more efficiently search for a unique integer
by reducing the size of the array so that we need to search through less objects
in the array.

Write a function that takes in an array of integers and a target.
The function should return the index of the target from the array.
If the target does not exist in the array return -1

Psuedocode planning:

To implement we should first attempt to reduce the array. To do this we look for the
middle of the array and use the two pointer method to keep track of the beginning and
end of the array. If the middle integer of the array is less than the target that becomes
the first index. If the middle integer is greater than the target that integer becomes
the last index. We do this until we find the target which should be in the middle.

'''

def binarySearch(list, targetNum):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = 1 + (right -1) // 2
        if list[mid] == targetNum:
            return mid #index of targetNum
        elif list[mid] < targetNum: #middle becomes left 
            left = mid + 1
        else: #middle becomes right
            right = mid - 1
            
    return -1
    

listIndex = [1,2,3,4,5,6,7,8,9]

print(binarySearch(listIndex, 5))