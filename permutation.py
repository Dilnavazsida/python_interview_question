def permutations(lst):
    if len(lst) == 1:
        return [lst]
      
    result = []

    for i in range(len(lst)):
        current = lst[i]
        remaining = lst[:i] + lst[i+1:]

        for perm in permutations(remaining):
            result.append([current] + perm)

    return result
  
print(permutations([1,2,3]))


# Another Way 

from itertools import permutations

l1 = [1,2,3]
lst = list(permutations(l1))
print(lst)

