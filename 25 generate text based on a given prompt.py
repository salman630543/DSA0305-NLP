import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key'

def generate_text(prompt, max_tokens=50, temperature=0.7):
    response = openai.Completion.create(
        engine="davinci",  # You can choose other engines too
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = "Once upon a time, there was a wise old wizard who lived in a tall tower. He spent his days..."
    generated_text = generate_text(prompt)

    print("Generated Text:")
    print(generated_text)
