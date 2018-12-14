n = 10
cache = [None] * (n-1)

def fib(n):
    # base case 
    if n==0 or n==1:
        return n
    # if n is in cache returns n
    if cache[n] != None:
        return cache[n]
    #extends the cache
    cache[n] = fib(n-1) + fib(n-2)
    
    return cache[n]
