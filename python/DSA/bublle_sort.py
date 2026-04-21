# 冒泡排序算法
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
bubble_sort(my_array)
print("Sorted array is:", my_array)