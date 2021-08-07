arr = [9,4,2,3,1,6,5,8,0,7]

def InsertionSort(arr):
    for i in range(len(arr)-1):
        for x in range(len(arr)-1-i):
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]
    return arr
print(InsertionSort(arr))