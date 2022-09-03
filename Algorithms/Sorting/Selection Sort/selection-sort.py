def selection_sort(arr):
  for i in range(len(arr)):
    min = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min]:
        min = j
    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp

  return arr

sorted_arr = selection_sort([-2, 45, 0, 11, -9,88,-97,-202,747])
print(sorted_arr)

# Time Complexity: O(n^2)
# Space Complexity: O(1)