# 线性排序
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [5, 3, 2, 8, 1]
target = 4
result = linearSearch(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")