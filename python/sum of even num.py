def sum_even_numbers(n):
    sum = 0
    for i in range(2, n+1, 2):
        sum += i
    return sum


n = 10
print(sum_even_numbers(n))