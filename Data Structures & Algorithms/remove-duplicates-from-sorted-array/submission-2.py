class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        num_len = len(nums)
        i = 0
        while(i < num_len - 1):
            if nums[i] == nums[i+1]:
                nums.pop(i + 1)
                num_len -= 1
                i -= 1
            i += 1

        return len(nums)