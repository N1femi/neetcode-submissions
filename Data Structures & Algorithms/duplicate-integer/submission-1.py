class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not list(set(nums)) == nums