# Questions:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


            #  simple way


# def two_sum(num,target):

#     for i in range(len(num)):
#         for j in range(i+1,len(num)):
#             if num[i] + num[j] == target:
#                 return i,j
# num = [2,7,11,15]
# target = 9
# print(two_sum(num,target))


                    # with functional way


# def twoSum(nums,target):

#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return i , j
# nums = [2,7,11,15]
# target = 9

# print(twoSum(nums,target))


                # object-orinted way

class Solution():

        def __init__(self,nums,target):
                self.nums = nums
                self.target = target
 
        def twoSum(nums,target):
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i] + nums[j] == target:
                        return i , j

b = Solution([2,7,11,15],9)
print(b.twoSum())
