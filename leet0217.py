# 0217. Contains Duplicate
# - Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# ----------------------------------------------------------------------
# Clarifications:
# 1 <= nums.length <= 105;  -109 <= nums[i] <= 109

# Inputs:
#nums = [1,1,1,3,3,4,3,2,4,2] # true
nums = [1,2,3,3]
nums = [1,2,3,2]
nums = [1,2,3,4]


# ----------------------------------------------------------------------
# Sol1: O() / O()
n = len(nums)
dic = {}
ans = False
for i in nums:
    if i in dic.keys():                # if seen before
        ans = True        
    else:
        dic[i] =+ 1             # inc count




# ----------------------------------------------------------------------
# Submit: Sol1, O() / O()
class Solution:
    def containsDuplicate(self, nums: list):
        #n = len(nums)
        dic = {}        
        for i in nums:
            print(i, list(dic.keys()))
            if i in list(dic.keys()):                # if seen before
                return True            
        return False                    # if no duplicates found

# --------------
# Test:
sol = Solution()
print(sol.containsDuplicate(nums))



