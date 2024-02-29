from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

def lesk_algorithm(word, sentence):
    # Tokenize the sentence and remove stopwords
    sentence_tokens = [token.lower() for token in word_tokenize(sentence) if token not in stopwords.words('english') and token not in string.punctuation]

    best_sense = None
    max_overlap = 0

    # Iterate over the synsets of the target word
    for sense in wordnet.synsets(word):
        # Get definition and example of the sense
        signature = word_tokenize(sense.definition())
        signature += [token.lower() for token in word_tokenize(sense.examples())]

        # Calculate the overlap between the signature and the sentence
        overlap = len(set(signature) & set(sentence_tokens))

        # Update the best sense if the overlap is higher
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense

if __name__ == "__main__":
    word = input("Enter a word: ")
    sentence = input("Enter a sentence: ")

    # Perform word sense disambiguation using the Lesk algorithm
    sense = lesk_algorithm(word, sentence)

    if sense:
        print(f"Word Sense: {sense.name()}")
        print(f"Definition: {sense.definition()}")
    else:
        print("No sense found for the word in the given sentence.")
