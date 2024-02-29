import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    # Process the text using SpaCy
    doc = nlp(text)

    # Iterate over the entities recognized by SpaCy
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Type: {ent.label_}")

if __name__ == "__main__":
    # Sample text for Named Entity Recognition
    text = "Apple is looking at buying U.K. startup for $1 billion"

    # Perform Named Entity Recognition
    perform_ner(text)
