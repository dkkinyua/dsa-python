# This function get the number in question in the array and returns its index and number too. Uses linear search and has a time complexity O(n) as it has order of n to run iterations on and its easier to use this linear search to get the number rather than a binary search.

def get_n(arr, n):
    for index in range(len(arr)):
        if arr[index] == n:
            return f"Number's index: {index}, number = {arr[index]}"
        
print(get_n([2,3,4,5,6,7], 3))
        
    
