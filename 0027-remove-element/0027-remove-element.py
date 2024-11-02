class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # dont use .pop or .insert, instead use 
        # a pointer-increment and indexing
        index_position = 0
        for i in range(len(nums)):
            if nums[i] != val:
                # nums[i]=nums[index_position] #2 = nums[0]
                nums[index_position] = nums[i]
                index_position +=1
                # print(nums[:nums[i]])
        return index_position