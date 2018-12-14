def fib_iter(n):
    a = 0
    b = 1
    
    for i in range(n):
       # a, b = b, a + b
        temp_a = a
        a = b
        b = temp_a + b
    return a
