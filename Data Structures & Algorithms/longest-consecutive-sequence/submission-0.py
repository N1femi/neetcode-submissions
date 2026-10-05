class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Understand: Given a list of numbers, return the longest consecutive sequence that can be formed
        Match: Longest Substring problem
        Plan:
        Implement:
        Review:
        Evaluate:
        """

        nums = set(nums)
        longest = 0

        for num in nums:
            #checks for sequence start
            length = 0

            if (num - 1) not in nums:
                while (num + length) in nums:
                    length += 1
                
                longest = max(longest, length)
        
        return longest