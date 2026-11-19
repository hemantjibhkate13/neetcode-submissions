class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                right_operand = stack.pop()
                left_operand = stack.pop()

                if token == "+":
                    res = left_operand + right_operand
                elif token == "-":
                    res = left_operand - right_operand
                elif token == "*":
                    res = left_operand * right_operand
                else:
                    res = int(left_operand / right_operand)

                stack.append(res)
            else:
                num = int(token)
                stack.append(num)

        return stack[-1]