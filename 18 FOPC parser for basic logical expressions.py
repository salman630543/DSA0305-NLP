class FOPCParser:
    def __init__(self):
        self.symbols = {'and': '&', 'or': '|', 'not': '~', '(': '(', ')': ')'}

    def parse_expression(self, expression):
        tokens = expression.split()
        postfix = self.infix_to_postfix(tokens)
        return self.evaluate_postfix(postfix)

    def infix_to_postfix(self, tokens):
        output = []
        stack = []

        for token in tokens:
            if token in self.symbols:
                if token == '(':
                    stack.append(token)
                elif token == ')':
                    while stack and stack[-1] != '(':
                        output.append(stack.pop())
                    stack.pop()  # Discard '('
                else:
                    while (stack and stack[-1] != '(' and 
                           self.precedence(stack[-1]) >= self.precedence(token)):
                        output.append(stack.pop())
                    stack.append(token)
            else:
                output.append(token)

        while stack:
            output.append(stack.pop())

        return output

    def precedence(self, op):
        if op in {'~'}:
            return 3
        elif op in {'&'}:
            return 2
        elif op in {'|'}:
            return 1
        else:
            return 0

    def evaluate_postfix(self, postfix):
        stack = []

        for token in postfix:
            if token in self.symbols:
                if token == '~':
                    operand = stack.pop()
                    stack.append(not operand)
                else:
                    operand2 = stack.pop()
                    operand1 = stack.pop()

                    if token == '&':
                        stack.append(operand1 and operand2)
                    elif token == '|':
                        stack.append(operand1 or operand2)
            else:
                stack.append(token == 'True')

        return stack[0]


if __name__ == "__main__":
    parser = FOPCParser()
    expression = input("Enter a logical expression: ")
    result = parser.parse_expression(expression)
    print(f"Result: {result}")
