# An important pre-condition for all search algorithms is to verify if the size of the array is not zero, n > 0
# Another one is to check if its ordered 




def sequential_search(array, target):
    for i in range(len(array)):  
        if array[i] == target:  
            return i
    return -1

array = [10, 20, 30, 40, 50]  
target = 30  

result = sequential_search(array, target)

if result != -1:
    print(f"Value found at: {result}")
else:
    print("Value not found")




#Input: array '[1... N]'
#Output: target int value 

#Pre-condition 1: n >= 1, as n being the size of the array
#Pre-condition 2: all of the elements must be ordered


# Init: We define both variables, x = 0 and y = len(array) - 1, so if the target value is inside the array
# it must be between the first position of the array til the last one, a[0...n-1] as 'n' being 'len(array)'

# Maintenance: if 'target < m', if it exists, it is lesser than 'm', left side. so we assign 'y' to be equal to 'm - 1'. 
# the new interval must be between 'array[0...m-1]'
# A similar issue will be when target > m, it is bigger than m and is gonna be in the right side. we assign in this case
# 'x' to be 'x=m+1' and the new interval is gonna be 'array[m+1 ... y]'
# if 'target == array[m]' then we return the index 'm' and found the target value
# In all of those cases, if the target value is inside the array, it continues to be in the interval from '[x - y]' maintaning 
# the invariant property

# Finishing: the search stops when 'x > y', that happens when the target value is definitely not inside the array
# in any of the new intervals, then the algorithm returns '-1'. In this case, if the interval is empty 'x > y' we can
# conclude target is not inside the array

# Theorem: T(n) = a·T(n/b) + f(n)
# T(n) = 1·T(n/2) + f(n), f(n) is gonna be Θ(1), because outside of the recursive calls, we don't depend on the size
# of the input to do the job itself

# We calculate  n^(log_b(a)) =>
# n^(log_2(1)) == 0
def binary_search(array, target): # only one recursive call, in the master theorem 'a = 1'
    x = 0
    y = len(array) - 1
    while x<=y:
        m = x + ((y-x)//2) 
        if target > array[m]: # we divide the problem in half, so 'b = 2'
            x= m + 1
        if target < array[m]:
            y = m -1
        else:
            return m
    return -1

array = [10, 20, 30, 40, 50]  
target = 30  

result_binary = binary_search(array, target)

if result_binary != -1:
    print(f"Value found at: {result_binary}")
else:
    print("Value not found")



# sequentialSearch(V, v)
## V is the array itself, while v is the target value
#    n ← size(V)
#    for i from 1 to n do
#        if V[i] == v then
#            return i
#    return -1



