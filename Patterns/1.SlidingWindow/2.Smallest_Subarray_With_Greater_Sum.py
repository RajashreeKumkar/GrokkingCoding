'''
Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray
whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].
'''

def smallest_size_sum(arr,k):
    res=100000
    start=0
    sum=0
    for end in range(len(arr)):
        sum+=arr[end]
        while sum>=k:
            res= min(res, end-start+1)
            sum-=arr[start]
            start+=1
    return res

if __name__=='__main__':
    arr=[2, 1, 5, 2, 3, 2]
    print(smallest_size_sum(arr, 7))