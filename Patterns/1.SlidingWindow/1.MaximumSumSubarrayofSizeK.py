
'''Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous
subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
'''



def maximumSum(arr,k):
    res=0
    start=0
    window_sum=0
    for end in range(len(arr)):
        window_sum += arr[end]
        if end>k-1:
            window_sum-=arr[start]
            start+=1
        res=max(res, window_sum)
    return res;


if __name__ =='__main__':
    #arr=[2,1,5,2,3,2]
    #arr = [2, 1, 5, 2, 8]
    arr = [2, 1, 5, 1, 3, 2]
    print(maximumSum(arr, 3))