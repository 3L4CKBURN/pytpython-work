def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(limit):
    sum = 0
    for num in range(2, limit+1):
        if is_prime(num):
            sum += num
    return sum

# example usage
print(sum_of_primes(100))
