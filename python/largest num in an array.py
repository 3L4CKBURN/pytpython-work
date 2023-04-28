def find_second_largest(arr):
    max_val = arr[0]
    second_max_val = float('-inf')
    for val in arr:
        if val > max_val:
            second_max_val = max_val
            max_val = val
        elif val > second_max_val and val != max_val:
            second_max_val = val
    return second_max_val
arr = [5, 10, 3, 8, 1]

print(find_second_largest(arr))
