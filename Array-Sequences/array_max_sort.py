#given array, and max integer in array, sort the array

import timeit
arr = [1,2,3,5,2,3,1,5,4,8,8,9]
def a(a):
    
    b = [0] * (9+1)

    for i in a:
        b[i]+=1
    s = []
    print a
    print b
    for p,c in enumerate(b):
        print p , c
        for t in range(c):
        
            s.append(p)
            print s

a(arr)
