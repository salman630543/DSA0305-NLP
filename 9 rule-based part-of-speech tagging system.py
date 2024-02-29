import re

# Sample text
text = "The cat sat on the mat. The dog barked at the cat."

# Define regular expression patterns for POS tagging
patterns = [
    (r'\b(?:The|the|A|a|An|an)\b', 'DET'),  # Determiners
    (r'\b(?:cat|dog|mat)\b', 'NOUN'),        # Nouns
    (r'\b(?:sat|barked)\b', 'VERB'),         # Verbs
    (r'\b(?:on|at)\b', 'PREP')               # Prepositions
]

# Function to perform rule-based POS tagging
def rule_based_pos_tagging(text, patterns):
    tagged_words = []
    for word in text.split():
        for pattern, tag in patterns:
            if re.match(pattern, word):
                tagged_words.append((word, tag))
                break
        else:
            tagged_words.append((word, 'UNK'))  # Assign 'UNK' tag for unknown words
    return tagged_words

# Perform rule-based part-of-speech tagging
tagged_text = rule_based_pos_tagging(text, patterns)

# Print the tagged words
print("Word\t\tPOS Tag")
print("------------------------")
for word, pos_tag in tagged_text:
    print(f"{word}\t\t{pos_tag}")
