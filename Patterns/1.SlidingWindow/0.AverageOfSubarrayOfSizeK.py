
'''
Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Here, we are asked to find the average of all subarrays of ‘5’ contiguous elements in the given array.
'''

#no sliding window
def getAverage(arr, k):
    res=[]
    for i in range(0,len(arr)-k+1):
        sum=0.0
        for j in range(i,i+k):
            sum+=arr[j]
        res.append(sum/k)
    print(res)
    return res;

#with sliding window

def slidingAverage(arr,k):
    res=[]
    sum=0.0
    start=0
    for end in range(len(arr)):
        sum+=arr[end]
        if end>=k-1:
            res.append(sum/k)
            sum-=arr[start]
            start+=1
    print(res)
    return res;


if __name__ =='__main__':
    #arr=[2,1,5,2,3,2]
    #arr = [2, 1, 5, 2, 8]
    arr = [3,4,1,1,6]
    print(slidingAverage(arr, 2))