# 2 SUM
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return [i, j]


# print(Solution().twoSum([0, 1, 3, 6], 9))

# PALINDROME
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str[x] == str[::-1]
