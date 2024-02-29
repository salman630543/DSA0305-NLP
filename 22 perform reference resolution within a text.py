def resolve_references(text):
    sentences = text.split('.')
    resolved_text = ""

    antecedent = None

    for sentence in sentences:
        tokens = sentence.split()
        resolved_sentence = []

        for token in tokens:
            if token.lower() in {'he', 'she', 'it', 'they', 'him', 'her', 'them'}:
                if antecedent:
                    resolved_sentence.append(antecedent)
                else:
                    resolved_sentence.append(token)
            elif token.lower() in {'is', 'was', 'were', 'am', 'are', 'has', 'have', 'had'}:
                antecedent = None
            else:
                if antecedent is None:
                    antecedent = token

            resolved_sentence.append(token)

        resolved_text += ' '.join(resolved_sentence) + '. '

    return resolved_text.strip()


if __name__ == "__main__":
    text = "John met Mary. She was happy. He gave her a flower. They walked together."
    resolved_text = resolve_references(text)
    print(resolved_text)
