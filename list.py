# def comman(l1,l2):
#     for i in range(len(l1)):
#         for j in range(len(l2)):
#             if l1[i] == l2[j]:
#                 return (l1[i])
            
# l1 = ['russia','india','bhutan']
# l2 = ['india','hongkong','pakistan']

# comman_value = comman(l1,l2)
# print(comman_value)



# lst1 = [1,2,3,4,5,6,7,8]
# even = []
# odd = []
# for i in range(len(lst1)):
#     if lst1[i] % 2 == 0:
#         even.append(lst1[i])
#     else:
#         odd.append(lst1[i])
# print(even)
# print(odd)



# l1 = [1,5,6,7,5,5,10]

# mn = min(l1)
# mx = max(l1)

# print(mn)
# print(mx)


# Write a Python program to find the maximum and minimum number in a list without using max() or min().

# l1 = [1,5,6,7,5,5,10]
# min = l1[0]
# max = l1[0]

# for i in l1:
#     if i < min:
#         min = i
#     if i > max:
#         max = i

# print(min)
# print(max)
        

# Given a list of numbers, create a new list with only even numbers.

# l1 = [1,5,6,7,5,5,10]

# even = []

# for i in l1:
#     if i % 2 == 0:
#         even.append(i)
# print(even)


# Count how many times each element occurs in a list using a dictionary.

# l = [1, 2, 2, 3, 4, 4, 4, 5]

# count_dict = {}

# for i in l:
#     if i in count_dict:
#         count_dict[i] += 1
#     else:
#         count_dict[i] = 1
# print(count_dict)



# Merge two dictionaries into one.

# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}

# 1st way
# d1.update(d2)
# print(d1)

# 2nd way
# mearge = {**d1 ,**d2}
# print(mearge)

# 3rd way
# mearge = d1 | d2
# print(mearge)


# Write a Python program to remove duplicates from a list while keeping the order same.

# l1 = [1,2,2,3,5,6,6,8,9,5]

# unique = []

# for i in l1:
#     if i not in unique:
#         unique.append(i)
# print(unique)



            # Given a dictionary of student marks, find the student with the highest marks.

# marks = {"Aman": 85, "Riya": 92, "Jay": 88}

# key = None
# value = 0

# for nm,sc in marks.items():
#     if sc > value:
#         value = sc
#         key = nm
# print(key)



            # Write a Python program to reverse a dictionary (keys become values, values become keys).

# d = {"a": 1, "b": 2, "c": 3}

# d1 = {}

# for k,v in d.items():
#     d1[v] = k

# print(d1)

# # Output → {1: "a", 2: "b", 3: "c"}



            # From a list of words, create a dictionary where key = word, value = length of the word.

# words = ["python", "django", "react"]

# n1 = {}

# for i in words:
#     n1[i] = len(i)
# print(n1)

# Output → {'python': 6, 'django': 6, 'react': 5}



                # Write a Python program to find common elements between two lists and store them 
                # in a dictionary with frequency.

# l1 = [1,2,3,4,5,5,6]
# l2 = [4,5,5,6,7]

# d1 = {}
# for i in l1:
#        if i in l2:
#            if i in d1:
#                 d1[i] += 1
#            else:
#                 d1[i] = 1
# print(d1)


# Output → {4:1, 5:2, 6:1}