# given a list of integers and target number, 
#write a function that returns a boolean indicating 
#if its possiple to sum two integers from the list ot reach the target number.
#you can not use integer element twice, optimise for time

def solutoin(a,t):
""" args: a = array
          t = target number
          returns boolean
          
          question:
                  return True if any two number is array sum to target number,=
  
"""
    seen = set()
    for num in a:
        num2 = t-num
        print("checking if num2 ",num2, " in set ",seen)
        if num2 in seen:
            print("num2 ",num2 ," found in set ",seen)
            print("here we go: ", t, num,num2)
            print(seen)
            return True
        
        seen.add(num)
        print("adding num1 ", num, " in set ",seen)
    print(seen)
    return False
