class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        U nderstand: Given an array of integers nums and n integer target look for 2 indices inside of the array that add to the target, return the smallest of the 2 first. You CANNOT use the same index twice.
        M atch: I remember how we can pair mathmatical ideas with the fact that the input array nums is SORTED.
        P lan: 
            Concerns:
                1. Are all input arrays sorted?
                2. What if the distinct indexes have the same number value, which would be returned first?
                3. How would we ensure no values are missed

        I mplement:
        R eview:
        E valuate:
        
        """

        seen = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in seen:
                return [seen[diff], i]
            seen[val] = i
