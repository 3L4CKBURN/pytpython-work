def sum_of_even_or_odd_numbers(limit, is_even=True):
    sum = 0
    for num in range(1, limit):
        if is_even and num % 2 == 0:
            sum += num
        elif not is_even and num % 2 != 0:
            sum += num
    return sum


print(sum_of_even_or_odd_numbers(10, True))  
print(sum_of_even_or_odd_numbers(10, False)) 
