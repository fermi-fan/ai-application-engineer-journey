myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(myArray)
exp = 1

while maxVal // exp > 0:

    while len(myArray) > 0:
        val = myArray.pop()
        radixIndex = (val // exp) % 10
        radixArray[radixIndex].append(val)

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            myArray.append(val)

    exp *= 10

print("Sorted array:", myArray)


# Radix Sort Algorithm with Bubble Sort as the Subroutine

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def radixSortWithBubbleSort(arr):
    maxVal = max(arr)
    exp = 1        
    while maxVal // exp > 0:
        radixArray = [[] for _ in range(10)]
        for val in arr:
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)
        for bucket in radixArray:
            bubbleSort(bucket)

        i = 0        
        for bucket in radixArray:
            for val in bucket:
                arr[i] = val
                i += 1
        exp *= 10

myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixSortWithBubbleSort(myArray)
print("Sorted array:", myArray)        