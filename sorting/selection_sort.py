def selection_sort(arr):
    for n in range(len(arr)-1,0,-1):
        maxPos = 0
        
        for k in range(n+1):
            if arr[k] > arr[maxPos]:
                maxPos = k
        
        temp = arr[k]
        arr[k] = arr[maxPos]
        arr[maxPos] = temp
        
