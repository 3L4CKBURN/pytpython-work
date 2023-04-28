def fibonacci_series(limit):
   
    a, b = 0, 1
    
   
    print(a, b, end=" ")
    
    
    while b < limit:
        c = a + b
        print(c, end=" ")
        a = b
        b = c


fibonacci_series(100)
