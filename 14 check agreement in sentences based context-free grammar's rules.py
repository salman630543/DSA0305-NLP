class AgreementChecker:
    def __init__(self, grammar):
        self.grammar = grammar

    def check_agreement(self, sentence):
        parse_tree = self.parse_sentence(sentence.split())
        return self.traverse_tree(parse_tree)

    def parse_sentence(self, sentence_tokens):
        # Simplified parsing, can be replaced with a more robust parser
        if len(sentence_tokens) == 2 and sentence_tokens[0] in self.grammar['noun'] and \
                sentence_tokens[1] in self.grammar['verb']:
            return (sentence_tokens[0], sentence_tokens[1])
        else:
            return None

    def traverse_tree(self, parse_tree):
        if parse_tree:
            subject, verb = parse_tree
            if self.grammar['noun'][subject] == self.grammar['verb'][verb]:
                return True
        return False


# Example usage:
if __name__ == "__main__":
    # Define the grammar
    grammar = {
        'noun': {
            'dog': 'singular',
            'dogs': 'plural',
            'cat': 'singular',
            'cats': 'plural'
        },
        'verb': {
            'runs': 'singular',
            'run': 'plural',
            'jumps': 'singular',
            'jump': 'plural'
        }
    }

    # Create an agreement checker
    agreement_checker = AgreementChecker(grammar)

    # Test sentences
    sentences = [
        "dog runs",
        "dogs run",
        "cat jumps",
        "cats jump"
    ]

    # Check agreement for each sentence
    for sentence in sentences:
        if agreement_checker.check_agreement(sentence):
            print(f"Agreement is correct in the sentence: '{sentence}'")
        else:
            print(f"Agreement is incorrect in the sentence: '{sentence}'")
