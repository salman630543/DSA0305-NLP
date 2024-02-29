import re

def recognize_dialog_acts(utterance):
    if re.match(r'.*\b(hi|hello|hey)\b.*', utterance, re.IGNORECASE):
        return "Greeting"
    elif re.match(r'.*\b(yes|yeah|sure|ok|okay)\b.*', utterance, re.IGNORECASE):
        return "Agreement"
    elif re.match(r'.*\b(no|nope|nevermind)\b.*', utterance, re.IGNORECASE):
        return "Disagreement"
    elif re.match(r'.*\b(thanks|thank you)\b.*', utterance, re.IGNORECASE):
        return "Thanking"
    elif re.match(r'.*\b(sorry|apologies)\b.*', utterance, re.IGNORECASE):
        return "Apologizing"
    elif re.match(r'.*\b(can you|could you|would you)\b.*', utterance, re.IGNORECASE):
        return "Requesting"
    elif re.match(r'.*\b(what|where|when|who|why|how)\b.*', utterance, re.IGNORECASE):
        return "Question"
    else:
        return "Statement"

if __name__ == "__main__":
    # Sample conversation
    conversation = [
        "Hello, how are you?",
        "I'm good, thank you. How about you?",
        "I'm doing well too, thanks.",
        "Can you help me with this?",
        "Sure, what do you need?",
        "I need some assistance with this Python program.",
        "No problem, I can help with that.",
        "Thanks a lot for your help!",
        "You're welcome!"
    ]

    # Recognize dialog acts for each utterance
    for utterance in conversation:
        dialog_act = recognize_dialog_acts(utterance)
        print(f"'{utterance}' - {dialog_act}")
