class State:
    def __init__(self, rule, dot, start_column):
        self.rule = rule
        self.dot = dot
        self.start_column = start_column

    def __eq__(self, other):
        return self.rule == other.rule and self.dot == other.dot and self.start_column == other.start_column

    def __str__(self):
        rule_str = ' '.join(self.rule)
        dotted_rule = ' '.join(self.rule[:self.dot] + ['•'] + self.rule[self.dot:])
        return f"{rule_str} -> {dotted_rule}, {self.start_column}"


class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.chart = []

    def parse(self, input_string):
        self.chart = [[] for _ in range(len(input_string) + 1)]
        self.predict(0)
        for i in range(len(input_string) + 1):
            self.scan(input_string, i)
            self.complete(i)

    def predict(self, column):
        for production in self.grammar:
            left, right = production.split(' -> ')
            right = right.split()
            state = State(right, 0, column)
            self.chart[column].append(state)

    def scan(self, input_string, column):
        if column >= len(input_string):
            return
        for state in self.chart[column]:
            if state.dot < len(state.rule) and state.rule[state.dot] == input_string[column]:
                self.chart[column + 1].append(State(state.rule, state.dot + 1, state.start_column))

    def complete(self, column):
        for state in self.chart[column]:
            if state.dot == len(state.rule):
                for st in self.chart[state.start_column]:
                    if st.dot < len(st.rule) and st.rule[st.dot] == state.rule[0]:
                        self.chart[column].append(State(st.rule, st.dot + 1, st.start_column))

    def parseable(self, input_string):
        self.parse(input_string)
        for state in self.chart[-1]:
            if state.rule == ['S', 'E'] and state.dot == 2:
                return True
        return False


# Example usage:
if __name__ == "__main__":
    grammar = [
        'S -> E',
        'E -> E + T',
        'E -> T',
        'T -> int',
        'T -> ( E )'
    ]

    earley_parser = EarleyParser(grammar)
    input_string = "int + ( int )"
    if earley_parser.parseable(input_string.split()):
        print("The input string is parseable!")
    else:
        print("The input string is not parseable!")
