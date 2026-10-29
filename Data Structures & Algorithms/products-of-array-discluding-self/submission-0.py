class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """

        Understanding;
            Using int list nums[], I should return an num list output[] where output[i] is the product of everything EXCEPT 
            nums[i]

        1. Getting the total product through one pass in nums: O(n)
        2. Go back through the array dividing out each element and placing in output[i]: O(n)
        Above method isn't ideal because division by 0 is a possibility

        1. I could use 2 pointers on both sides of the element position in nums
        2. Extend both sides of nums by 1 element both being "1" to prevent multiplicative changes
        3. Start as l = 0 and r = -1
        4. Loop while getting total multiple and put that in output[i]
        """

        

        nums = [1] + nums + [1] # Extends bounds for pointer use
        output = [1] * (len(nums) - 2)

        for i in range(1, len(nums) - 1):
            total_product = 1

            l = 0
            r = len(nums) - 1

            while l < i:
                total_product *= nums[l]
                l += 1

            while r > i:
                total_product *= nums[r]
                r -= 1

            output[i - 1] = total_product

        
        return output


        