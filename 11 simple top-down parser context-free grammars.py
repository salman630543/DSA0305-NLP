class Parser:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, input_string):
        self.input = input_string
        self.index = 0
        self.current_token = None
        self.next_token()
        return self.parse_expression()

    def next_token(self):
        if self.index < len(self.input):
            self.current_token = self.input[self.index]
            self.index += 1
        else:
            self.current_token = None

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.next_token()
        else:
            raise Exception(f"Syntax error: expected {expected_token}, found {self.current_token}")

    def parse_expression(self):
        return self.parse_term() + self.parse_expression_tail()

    def parse_expression_tail(self):
        if self.current_token in ['+', '-']:
            op = self.current_token
            self.next_token()
            return op + self.parse_term() + self.parse_expression_tail()
        else:
            return ''

    def parse_term(self):
        return self.parse_factor() + self.parse_term_tail()

    def parse_term_tail(self):
        if self.current_token in ['*', '/']:
            op = self.current_token
            self.next_token()
            return op + self.parse_factor() + self.parse_term_tail()
        else:
            return ''

    def parse_factor(self):
        if self.current_token.isdigit():
            value = self.current_token
            self.match(self.current_token)
            return value
        elif self.current_token == '(':
            self.match('(')
            expression = self.parse_expression()
            self.match(')')
            return '(' + expression + ')'
        else:
            raise Exception(f"Syntax error: unexpected token {self.current_token}")


# Example usage:
if __name__ == "__main__":
    grammar = """
    expression -> term expression_tail
    expression_tail -> '+' term expression_tail | '-' term expression_tail | ε
    term -> factor term_tail
    term_tail -> '*' factor term_tail | '/' factor term_tail | ε
    factor -> NUMBER | '(' expression ')'
    """

    parser = Parser(grammar)
    input_string = "3 + 4 * (2 - 1)"
    result = parser.parse(input_string)
    print("Input:", input_string)
    print("Result:", result)
