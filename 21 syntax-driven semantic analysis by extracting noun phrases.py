import nltk
from nltk.corpus import wordnet

def extract_noun_phrases(sentence):
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)

    # Perform part-of-speech tagging
    tagged_tokens = nltk.pos_tag(tokens)

    # Extract noun phrases
    noun_phrases = []
    current_phrase = []

    for token, pos_tag in tagged_tokens:
        if pos_tag.startswith('NN'):  # Noun
            current_phrase.append(token)
        else:
            if current_phrase:
                noun_phrases.append(current_phrase)
                current_phrase = []

    # Add the last phrase if any
    if current_phrase:
        noun_phrases.append(current_phrase)

    return noun_phrases

def get_phrase_meanings(phrase):
    meanings = []
    for word in phrase:
        synsets = wordnet.synsets(word)
        if synsets:
            meanings.append(synsets[0].definition())
    return meanings

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")

    # Download WordNet if not already downloaded
    nltk.download('wordnet')

    # Extract noun phrases from the sentence
    noun_phrases = extract_noun_phrases(sentence)

    # Get meanings for each noun phrase
    for phrase in noun_phrases:
        meanings = get_phrase_meanings(phrase)
        print(f"Noun Phrase: {' '.join(phrase)}")
        print("Meanings:")
        for meaning in meanings:
            print(f" - {meaning}")
