from transformers import T5ForConditionalGeneration, T5Tokenizer

def translate_text(text, model, tokenizer):
    # Tokenize the input text
    inputs = tokenizer.encode("translate English to French: " + text, return_tensors="pt")

    # Generate translation
    outputs = model.generate(inputs, max_length=100, num_beams=4, early_stopping=True)

    # Decode the generated translation
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return translated_text

if __name__ == "__main__":
    # Load pre-trained model and tokenizer
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    tokenizer = T5Tokenizer.from_pretrained("t5-base")

    # Input English text
    english_text = "Hello, how are you?"

    # Translate English text to French
    french_translation = translate_text(english_text, model, tokenizer)

    print("English Text:", english_text)
    print("French Translation:", french_translation)
