class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val not in {"+", "-", "/", "*"}:
                stack.append(int(val))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                currResult = 0

                if val == "+":
                    currResult = operand1 + operand2
                elif val == "-":
                    currResult = operand1 - operand2
                elif val == "*":
                    currResult = operand1 * operand2
                elif val == "/":
                    currResult = int(operand1 / operand2)
                
                stack.append(currResult)

        
        return stack[0]
                    

        
        