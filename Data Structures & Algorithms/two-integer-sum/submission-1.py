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

            Assuming input arrays are sorted, we can place two pointers in the array, one at the beginning and one at the end, because the array is sorted we would be able to do the following:
            - If startPointer + endPointer > target; we can move end pointer down because doing so reduces the sum and we dont miss any possible combination since if we moved startPointer up we would be increasing(or keeping it the same is the next value is the same) the sum.
            - If startPointer + endPointer < target; we would move startPointer up to increae the sum, it's ensured we dont miss a combination since every we HAVEN't covered is inward, but if we find out 2 values theres no need to keep checking if we still have more.

        I mplement:
        R eview:
        E valuate:
        
        """

        leftPointer = 0
        rightPointer = (len(nums) - 1)

        while leftPointer < rightPointer:
            currSum = nums[leftPointer] + nums[rightPointer]

            if currSum < target:
                leftPointer += 1
            elif currSum > target:
                rightPointer -= 1
            elif currSum == target:
                return [leftPointer, rightPointer]


