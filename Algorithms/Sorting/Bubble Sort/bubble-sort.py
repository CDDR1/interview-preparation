def bubble_sort(arr):
  sorted = False
  n = len(arr) - 1

  while not sorted:
    sorted = True
    for i in range(n):
      if arr[i] > arr[i + 1]:
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp
        sorted = False
    n -= 1

  return arr

sorted_arr = bubble_sort([-2, 45, 0, 11, -9,88,-97,-202,747])
print(sorted_arr)

# Time Complexity: O(n^2)
# Space Complexity: O(1)