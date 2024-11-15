'''
选择排序(Selection-sort)是一种简单直观的排序算法。它的工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
'''
def fun(arr):
    
    for i in range(len(arr)):
        min_id=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_id]:
                min_id=j
        arr[min_id],arr[i]=arr[i],arr[min_id]
    
    return arr
arr=[4,3,5,6,2,1,4]
print(fun(arr))