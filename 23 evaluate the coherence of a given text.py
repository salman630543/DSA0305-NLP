from collections import Counter

def evaluate_coherence(text):
    # List of common transition words indicating coherence
    transition_words = ["first", "second", "third", "finally", "next",
                        "meanwhile", "in addition", "furthermore", "however",
                        "therefore", "consequently", "thus", "as a result",
                        "in conclusion", "on the other hand", "moreover",
                        "nevertheless", "nonetheless", "accordingly", "so"]

    # Tokenize the text into words
    words = text.split()

    # Count the occurrence of transition words
    word_count = Counter(words)

    # Calculate the coherence score based on the frequency of transition words
    coherence_score = sum(word_count[word] for word in transition_words)

    return coherence_score

if __name__ == "__main__":
    text = input("Enter the text to evaluate coherence: ")

    # Evaluate coherence
    coherence_score = evaluate_coherence(text)

    print(f"Coherence Score: {coherence_score}")
