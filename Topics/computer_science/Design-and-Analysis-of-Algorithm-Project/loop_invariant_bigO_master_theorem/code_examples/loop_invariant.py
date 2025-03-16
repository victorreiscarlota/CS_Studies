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




# sequentialSearch(V, v)
## V is the array itself, while v is the target value
#    n ← size(V)
#    for i from 1 to n do
#        if V[i] == v then
#            return i
#    return -1
