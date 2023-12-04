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

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        
        # gets left and right of array to be sorted
        L = arr[:mid]
        R = arr[mid:]
        
        #recursion continues breaking down arrays to left and right
        print('left array: ', L, 'right array: ', R)
        mergeSort(L)
        mergeSort(R)

        merge(arr, L, mid, R)

        return arr
    else:
        return 'array is not bigger than one element', arr
        
def merge(arr, L, mid, R):

    # print('right array', R)
    #i is pointer to left array's first element
    #j is pointer to right array's first element
    #k is pointer to result merge's array's first element
    i = 0
    j = 0
    k = 0
    
    #merge(Sort) the arrays
    #while (i) first element of left array is not at end of left array
    #and while (j) first element of right array is not at end of right array
    #if first element of left array is smaller than first element of right array
    #put first element of left array to result array's pointer (first element)
    #move left pointer to second element of left array.
    #else if first element of right array is smaller than first element of left array
    #put first element of right array to result array's pointer (first element)
    #increment the pointer of result array to the 2nd (etc) element
    #repeat the above steps while you have a left and right array
    while i < len(L) and j < len(R):
        print('left array before sort: ', L)
        print('right array before sort: ', R)
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

        
    #when you don't have a left and right array (finished sorting)
    #append the rest of the array to the end
    #if there is no right array append the left array to the end of the result array
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        
            
testArr = [2,3,1,6,8,5,9,4,7]
testArr2 = [2]
testArr3 = []
print(mergeSort(testArr))
print(mergeSort(testArr2))
print(mergeSort(testArr3))