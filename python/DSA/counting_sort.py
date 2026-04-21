# 计数排序算法
def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    arr[:] = []
    for num, freq in enumerate(count):
        arr.extend([num] * freq)
    return arr    
my_array = [4, 2, 2, 8, 3, 3, 1]
counting_sort(my_array)
print("Sorted array is:", my_array)