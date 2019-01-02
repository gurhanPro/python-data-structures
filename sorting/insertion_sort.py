def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        
        currentvalue = arr[i]
        print(arr)
        while i > 0 and arr[i-1] > currentvalue:
            arr[i] = arr[i-1]
            i -=1
           
        a[i] = currentvalue
