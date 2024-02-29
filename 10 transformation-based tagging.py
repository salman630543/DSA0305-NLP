import nltk

# Download necessary NLTK resources (if not already downloaded)
nltk.download('punkt')

# Sample text
text = "The cat sat on the mat. The dog barked at the cat."

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Define transformation rules
transformation_rules = [
    (r'.*ing$', 'VERB'),   # Gerunds ending with 'ing' are verbs
    (r'.*ed$', 'VERB'),    # Past tense verbs ending with 'ed'
    (r'.*ly$', 'ADV'),     # Adverbs ending with 'ly'
    (r'^\d+$', 'NUM'),     # Numerals
    (r'.*', 'NOUN')        # Default tag: nouns
]

# Function to apply transformation rules for tagging
def apply_transformation_rules(word, rules):
    for pattern, tag in rules:
        if nltk.re.match(pattern, word):
            return tag
    return 'UNK'  # Assign 'UNK' tag for unknown words

# Apply transformation-based tagging
tagged_words = [(word, apply_transformation_rules(word, transformation_rules)) for word in words]

# Print the tagged words
print("Word\t\tPOS Tag")
print("------------------------")
for word, pos_tag in tagged_words:
    print(f"{word}\t\t{pos_tag}")
