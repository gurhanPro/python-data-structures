stable = 0
counter = 0
a = [-1,1,3,3,3,4,5,6,7]
for i in range(0,len(a)):
    if i < len(a) -2:
        if a[i+1]-a[i] == a[i+2] - a[i+1]:
            stable += 1
            counter +=1
        print(i)
    else: 
        print("out ",i)
print(stable)
