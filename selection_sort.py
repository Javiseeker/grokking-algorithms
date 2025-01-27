def find_smallest(array):
    smallest = array[0]
    smallest_index = 0

    for idx, item in enumerate(array):
        if item < smallest:
            smallest = item
            smallest_index = idx

    return smallest_index

def selection_sort(array):
    sorted = []
    for i in range(len(array)): # important to do a loop with the length of the array instead of enumerate(array)
        smallest = find_smallest(array)
        sorted.append(array.pop(smallest)) # here its removing smallest, then assigning to sorted.

    return sorted

my_array = [5,4,2,1, 10, 5]

print(selection_sort(my_array))