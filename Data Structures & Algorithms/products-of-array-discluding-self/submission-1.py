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
        Above WORKS, but TOO INEFFICIENT!

        1. Start with a multiplicand = 1, as i replace each element as I go with the multiplicand and multiply the 
        multiplicand by each element I pass
        2. In reverse multiply as we go starting with 1 continuing to multiply by passed values
        """

        n = len(nums)

        left_mult = 1
        right_mult = 1

        output = [1] * n

        for i in range(n): # Conceptually the multiplied value of everything on LEFT of element
            output[i] = left_mult 

            left_mult *= nums[i]


        for i in range(n-1, -1, -1):
            output[i] *= right_mult

            right_mult *= nums[i]
        
        return output



        