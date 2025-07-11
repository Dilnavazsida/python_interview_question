def sort_array_0_1_2(arr):

  low = 0
  mid = 0
  high = len(arr) -1

  while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low +=1
            mid +=1

        elif arr[mid] == 1:
            mid +=1

        else:
             arr[mid],arr[high] = arr[high],arr[mid]
             high -= 1
    
  return arr


arr = [1, 2, 0, 2, 1, 0]
print(sort_array_0_1_2(arr))
