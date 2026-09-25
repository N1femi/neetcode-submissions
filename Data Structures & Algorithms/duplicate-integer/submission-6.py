class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNums = set() # Look up on a Set vs. List is O(1) vs O(n)

        for num in nums:
            if num in seenNums:
                return True
            seenNums.add(num)

        
        return False