def insertion_sort(arr):
  for i in range(1, len(arr)):
    curr = arr[i]
    j = i
    while (j > 0) and (arr[j - 1] > curr):
      arr[j] = arr[j - 1]
      j -= 1 
    arr[j] = curr  

  return arr
  
sorted = insertion_sort([5, 9, 2, 6, 20, 4.3, -2, 14])
print(sorted)

# Time Complexity: O(n^2)
# Space Complexity: O(1)