
'''Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous
subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
'''



def maximumSum(arr,k):






if __name__ =='__main__':
    #arr=[2,1,5,2,3,2]
    #arr = [2, 1, 5, 2, 8]
    arr = [3,4,1,1,6]
    print(maximumSum(arr, 2))