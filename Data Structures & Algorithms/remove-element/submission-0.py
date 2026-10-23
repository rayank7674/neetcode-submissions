class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_len = len(nums)
        i = 0
        while i < num_len:
            if nums[i] == val:
                nums.remove(val)
                num_len -= 1
            else: i += 1
        return len(nums)