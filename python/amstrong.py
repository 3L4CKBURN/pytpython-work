def is_armstrong(num):
   
    n = 0
    temp = num
    while temp > 0:
        n += 1
        temp //= 10
    
    
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    
    
    return sum == num
number= int(input("enter a number : "))

if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number,"is not an Armstrong number")

