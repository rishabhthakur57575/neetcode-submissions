import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                second_number = res.pop()
                first_number = res.pop()

                if token == '+':
                    res.append(first_number + second_number)
                elif token == '-':
                    res.append(first_number - second_number)
                elif token == '*':
                    res.append(first_number * second_number)
                else:
                    res.append(int(first_number / second_number))
            else:
                res.append(int(token))

        return res[-1]