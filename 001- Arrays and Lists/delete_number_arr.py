# This function deletes a number in an array by getting the number's index and popping it out.
# Time complexity: O(n)
def remove_number(arr, n):
    for index in range(len(arr)):
        if arr[index] == n:
            arr.remove(arr[index])
            return arr
        

print(remove_number([2,3,4,5,6,7,8], 5))