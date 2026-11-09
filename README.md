# Spam Message Detector

A beginner machine learning project in Python. It learns from labelled messages and then predicts whether a new message is spam or not.

## How it works
1. **Data:** 40 short example messages (20 spam, 20 normal) in `data.py`.
2. **Text to numbers:** TF-IDF turns each message into numbers based on how important its words are.
3. **Model:** a Naive Bayes classifier learns which words point to spam.
4. **Test:** 25% of the messages are held back to check accuracy on messages the model has not seen.
5. **Try it:** type your own message and see the prediction and confidence.

## Run it
```bash
pip install -r requirements.txt
python spam_detector.py
```

Example:
```
Message: You won a free gift, click this link
  -> SPAM (confidence 71%)
Message: Are you coming to class tomorrow?
  -> NOT SPAM (confidence 67%)
```

## Limits
- The dataset is tiny, so the 90% accuracy is measured on only 10 test messages and is not reliable. Real spam filters train on thousands of messages.
- Confidence is low for the same reason. Adding more examples to `data.py` improves it.

## What I learned
- Splitting data into training and test sets
- Turning text into features with TF-IDF
- Training and evaluating a classifier with scikit-learn

## Next steps
- Train on a larger public dataset (for example, the SMS Spam Collection)
- Turn it into a FastAPI endpoint
- Add a simple web page for typing messages

Built with Python and scikit-learn.
