def generate_primes(limit):
    primes = []
    for num in range(2, limit+1):
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

limit = 20
print(generate_primes(limit)) 

arr = [5, 10, 3, 8, 1]
min_val, max_val = find_min_max(arr)
print("Minimum value:", min_val)
print("Maximum value:", max_val) 

