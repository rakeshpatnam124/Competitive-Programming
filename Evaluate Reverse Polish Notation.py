class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        res = []
        for element in tokens:
            match (element):
                case '+':
                    op2 = int(stack.pop())
                    op1 = int(stack.pop())
                    res = op1 + op2
                    stack.append(str(res))
                case '-':
                    op2 = int(stack.pop())
                    op1 = int(stack.pop())
                    res = op1 - op2
                    stack.append(str(res))
                case '*':
                    op2 = int(stack.pop())
                    op1 = int(stack.pop())
                    res = op1 * op2
                    stack.append(str(res))
                case '/':    
                    op2 = int(stack.pop())
                    op1 = int(stack.pop())
                    res = int(op1 / op2)
                    stack.append(str(res))
                case _:
                    stack.append(element)
        return int(stack.pop())
