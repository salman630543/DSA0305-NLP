class Node:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children else []

    def __str__(self):
        return self.label


class ParseTreeGenerator:
    def __init__(self, grammar):
        self.grammar = grammar
        self.parse_tree = None

    def generate_parse_tree(self, input_string):
        self.parse_tree = self.parse_input_string(input_string.split())

    def parse_input_string(self, input_tokens):
        if not input_tokens:
            return None

        root = Node('S')
        self.parse(root, input_tokens)
        return root

    def parse(self, node, input_tokens):
        if not input_tokens:
            return

        for production in self.grammar:
            left, right = production.split(' -> ')
            right_tokens = right.split()

            if node.label == left and input_tokens[:len(right_tokens)] == right_tokens:
                node.children = [Node(token) for token in right_tokens]
                for child in node.children:
                    self.parse(child, input_tokens[len(right_tokens):])
                return

    def print_parse_tree(self, node, level=0):
        if node is None:
            return

        print(' ' * level + str(node))
        for child in node.children:
            self.print_parse_tree(child, level + 1)


# Example usage:
if __name__ == "__main__":
    grammar = [
        'S -> NP VP',
        'NP -> Det N',
        'VP -> V NP',
        'Det -> the',
        'N -> cat',
        'V -> chased'
    ]

    parse_tree_generator = ParseTreeGenerator(grammar)
    input_string = "the cat chased"
    parse_tree_generator.generate_parse_tree(input_string)
    parse_tree = parse_tree_generator.parse_tree
    if parse_tree:
        print("Parse Tree:")
        parse_tree_generator.print_parse_tree(parse_tree)
    else:
        print("No parse tree generated for the input string.")
