class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    stack.append(-1 * stack.pop() + stack.pop())
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    stack.append(int(1 / stack.pop() * stack.pop()))
                case _:
                    stack.append(int(token))
        return int(stack.pop())
