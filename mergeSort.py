'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity
and with the smallest space complexity possible.

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104

Summary/Explanation:

We are given an array of integers and want to sort it in ascending order and then return it.
We cannot use any built-in sorting function. We should use a mergeSort algorithm for this.

Psuedocode planning:

To implement merge sort we first need to break down the array into a left and right array.
To do so we find the middle of the array and split the array into two using python's
[:midIndex] which returns a list from the beginning to the index before the mid index 
and [mid:] which returns a list from the mid index to the end index
We use recursion to call upon mergeSort again and again until we get to 1 element in the array.
We now have a sorted array and we know this because it is only one element in the array.
Now we go back and combine left side sorted array with the right side sorted array into a
bigger sorted array. We do this until we get back to a sorted array of the size of the original
array.
'''