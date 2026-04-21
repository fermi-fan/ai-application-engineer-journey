# 选择排序算法
my_array = [64, 34, 25, 5, 22, 11, 90, 12]
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
selection_sort(my_array)
print("Sorted array is:", my_array)