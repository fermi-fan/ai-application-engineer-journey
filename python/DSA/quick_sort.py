# 快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
sorted_array = quick_sort(my_array)
print("Sorted array is:", sorted_array)