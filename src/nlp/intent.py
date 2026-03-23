from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import numpy as np

class IntentClassifier:
    def __init__(self):
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', LogisticRegression())
        ])
        self.is_trained = False

    def train(self, training_data):
        """
        training_data: list of (text, label) tuples
        """
        texts, labels = zip(*training_data)
        self.pipeline.fit(texts, labels)
        self.is_trained = True

    def predict(self, text):
        if not self.is_trained:
            return "unknown"
        return self.pipeline.predict([text])[0]
