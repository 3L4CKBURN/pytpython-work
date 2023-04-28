def find_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    for val in arr:
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val
    return min_val, max_val

arr = [5, 10, 3, 8, 1]
min_val, max_val = find_min_max(arr)
print("Minimum value:", min_val) 
print("Maximum value:", max_val) 
