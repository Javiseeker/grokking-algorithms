def sumArrayRecursively(arr): # Divide n conquer
    if len(arr) == 0:
        return 0
    return arr.pop() + sumArrayRecursively(arr)

arr = [1, 2, 4, 5, 20]
result = sumArrayRecursively(arr)
print(f"result: {result}")