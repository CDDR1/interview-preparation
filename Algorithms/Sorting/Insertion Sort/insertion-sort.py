def insertion_sort(arr):
  for j in range(1, len(arr)):
    key = arr[j]
    i = j - 1
    while (i >= 0) and (arr[i] > key):
      arr[i + 1] = arr[i]
      i = i - 1
    arr[i + 1] = key
  
  return arr

sorted = insertion_sort([5, 9, 2, 6])
print(sorted)

# Time Complexity: O()
# Space Complexity: O(1)