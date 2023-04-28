def find_max(arr):
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val

    arr = [5, 10, 3, 8, 1]
print(find_max(arr)) 