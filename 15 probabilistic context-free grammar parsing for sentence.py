import nltk

class PCFGParser:
    def __init__(self, pcfg_grammar):
        self.pcfg_grammar = pcfg_grammar

    def parse(self, sentence):
        tokens = nltk.word_tokenize(sentence)
        parser = nltk.parse.ViterbiParser(self.pcfg_grammar)
        parses = list(parser.parse(tokens))
        if parses:
            # Return the most probable parse tree
            return parses[0].tree()
        else:
            return None


# Example usage:
if __name__ == "__main__":
    # Define a simple PCFG grammar
    pcfg_grammar_str = """
    S -> NP VP [1.0]
    VP -> V NP [0.7] | VP PP [0.3]
    PP -> P NP [1.0]
    NP -> Det N [0.6] | NP PP [0.4]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'man' [0.5] | 'dog' [0.3] | 'park' [0.2]
    V -> 'saw' [0.4] | 'ate' [0.3] | 'walked' [0.3]
    P -> 'in' [0.6] | 'with' [0.4]
    """

    # Load PCFG grammar
    pcfg_grammar = nltk.PCFG.fromstring(pcfg_grammar_str)

    # Create a PCFG parser
    parser = PCFGParser(pcfg_grammar)

    # Test sentence
    sentence = "the man saw a dog in the park"

    # Parse the sentence using PCFG parsing
    parse_tree = parser.parse(sentence)

    if parse_tree:
        print("Parse Tree:")
        print(parse_tree)
    else:
        print("Unable to parse the sentence.")
