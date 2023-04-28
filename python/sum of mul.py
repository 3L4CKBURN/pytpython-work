def sum_of_multiples(limit):
    sum = 0
    for num in range(1, limit):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum


print(sum_of_multiples(100))
