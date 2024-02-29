import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

def explore_word_meanings(word):
    # Retrieve synsets for the given word
    synsets = wordnet.synsets(word)

    if synsets:
        print(f"Synsets for '{word}':")
        for synset in synsets:
            print(f" - {synset.name()}: {synset.definition()}")

        # Explore hypernyms (more general words)
        hypernyms = synsets[0].hypernyms()
        if hypernyms:
            print(f"\nHypernyms of '{word}':")
            for hypernym in hypernyms:
                print(f" - {hypernym.name()}: {hypernym.definition()}")

        # Explore hyponyms (more specific words)
        hyponyms = synsets[0].hyponyms()
        if hyponyms:
            print(f"\nHyponyms of '{word}':")
            for hyponym in hyponyms:
                print(f" - {hyponym.name()}: {hyponym.definition()}")
    else:
        print(f"No synsets found for '{word}'")

if __name__ == "__main__":
    word = input("Enter a word to explore its meanings: ")
    explore_word_meanings(word)
