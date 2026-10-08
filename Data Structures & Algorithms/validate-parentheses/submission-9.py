class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) < 2:
            return False

        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
            elif len(stack) == 0 or ((i == ')' and stack[-1] != '(') or (i == ']' and stack[-1] != '[') or (i == '}' and stack[-1] != '{')):
                return False
            else:
                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False
