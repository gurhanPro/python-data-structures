def fib(n):
    """
        return the n fibonaci
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    #  fibonacci sequence: 0,1,1,2,3,5,8,13,21
