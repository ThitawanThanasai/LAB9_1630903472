def binary(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary(arr, low, mid - 1, x)
        else:
            return binary(arr, mid + 1, high, x)
    else:
        return -1

arr = [7,10,12,14,16,20,29,37]

x = 14
sum = binary(arr, 0, len(arr) - 1, x)
if sum != -1:
    print("Element is present at index", str(sum))
else:
    print("Element is not present in array")

x = 29
sum = binary(arr, 0, len(arr) - 1, x)
if sum != -1:
    print("Element is present at index", str(sum))
else:
    print("Element is not present in array")