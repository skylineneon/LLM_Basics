'''
从第一个元素开始，该元素可以认为已经被排序；
取出下一个元素，在已经排序的元素序列中从后向前扫描；
如果该元素（已排序）大于新元素，将该元素移到下一位置；
重复步骤3,直到找到已排序的元素小于或者等于新元素的位置；
将新元素插入到该位置后；
重复步骤2~5。
'''
def insertion_sort(arr):
    # 从第二个元素开始遍历数组
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # 将其与前面的元素比较，如果找到比其大的元素，就向后移动
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # 插入正确的位置
        arr[j + 1] = key 
    return arr  
arr1=[4,3,5,6,2,1]
print(insertion_sort(arr1))

        