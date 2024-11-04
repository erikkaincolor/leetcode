class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if nums.count(nums[i]) > 1:pop nums[i] to last [-1] and pop it...whatever pop returns, add that to a new list then at the end return that list...

        i = 0 #manual index
        dupes_array = []
        new_array = []
        while i < len(nums):
            if nums[i] in new_array:
                dupes_array.append(nums.pop(i)) #this is two steps in one since pop returns an index and removes, so really 3 steps
            else:
                new_array.append(nums[i]) #new array gets it first item here
                i+=1 #increment 1 only if its not a dupe
        nums[:] = new_array #copies all elem from new_array into nums

        # errors:
# [0,0,1,1,1,2,2,3,3,4] input
# [0,1,1,1,2,2,3,3,4] my ouput only popped 1 dupe at first
# [0,1,2,3,4] expected output
