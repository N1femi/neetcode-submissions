class Solution:
    def isValid(self, s: str) -> bool:
        """
        Plan:

        I'll have a stack and for each parenthesis in the string I'll check if stack isn't empty:

            If empty just insert:

            If not empty compare previous parenthesis index with current patenthesis index in other table
        """

        stack = []

        left = ["(", "[", "{"]
        right = [")", "]", "}"]

        for char in s:
            if len(stack) != 0:
                if stack[-1] in left:
                    targetIndex = left.index(stack[-1])
                    
                    if char in right:
                        if targetIndex == right.index(char):
                            stack.pop()
                            continue

            stack.append(char)

        return len(stack) == 0