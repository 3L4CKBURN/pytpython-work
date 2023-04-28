def sum_of_digits(num):
    # Initialize sum variable to 0
    sum = 0
    
    num_str = str(num)
   
    for digit in num_str:
        sum += int(digit)
    return sum


num = 12345
print(sum_of_digits(num)) 
