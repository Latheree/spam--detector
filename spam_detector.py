"""Spam Message Detector
A beginner machine learning project: teach a model to tell spam from normal messages.

How it works:
1. Turn each message into numbers (TF-IDF: how important each word is).
2. Train a Naive Bayes model on labelled examples.
3. Test it on messages it has never seen, then let you try your own.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

from data import MESSAGES, LABELS


def train_model():
    """Split the data, train the model, and report how well it does."""
    x_train, x_test, y_train, y_test = train_test_split(
        MESSAGES, LABELS, test_size=0.25, random_state=42, stratify=LABELS
    )
    model = make_pipeline(TfidfVectorizer(lowercase=True), MultinomialNB())
    model.fit(x_train, y_train)

    accuracy = accuracy_score(y_test, model.predict(x_test))
    print(f"Trained on {len(x_train)} messages, tested on {len(x_test)}.")
    print(f"Accuracy on unseen messages: {accuracy:.0%}\n")
    return model


def predict(model, text):
    """Return the label and the model's confidence for one message."""
    label = model.predict([text])[0]
    confidence = model.predict_proba([text]).max()
    return label, confidence


def main():
    model = train_model()
    print("Type a message to check it. Type 'quit' to stop.\n")
    while True:
        text = input("Message: ").strip()
        if text.lower() == "quit":
            break
        if not text:
            continue
        label, confidence = predict(model, text)
        print(f"  -> {label.upper()} (confidence {confidence:.0%})\n")


if __name__ == "__main__":
    main()
