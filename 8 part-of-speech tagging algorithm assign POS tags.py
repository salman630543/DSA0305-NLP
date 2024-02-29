import random

# Sample text
text = "The cat sat on the mat. The dog barked at the cat."

# Tokenize the text into words
words = text.split()

# Define the POS tag set
pos_tags = {
    'The': ['DET'],
    'cat': ['NOUN', 'VERB'],
    'sat': ['VERB'],
    'on': ['ADP'],
    'the': ['DET'],
    'mat.': ['NOUN'],
    'dog': ['NOUN', 'VERB'],
    'barked': ['VERB'],
    'at': ['ADP']
}

# Function to assign POS tags randomly based on the probabilities
def stochastic_pos_tagging(word):
    possible_tags = pos_tags.get(word, ['UNK'])  # If word not found, assign UNK (unknown)
    return random.choice(possible_tags)

# Perform stochastic part-of-speech tagging
pos_tagged_words = [(word, stochastic_pos_tagging(word)) for word in words]

# Print the tagged words
print("Word\t\tPOS Tag")
print("------------------------")
for word, pos_tag in pos_tagged_words:
    print(f"{word}\t\t{pos_tag}")
