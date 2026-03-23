from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

class KnowledgeRetriever:
    def __init__(self, data_path):
        self.vectorizer = TfidfVectorizer()
        self.data = self._load_data(data_path)
        self.questions = [item['question'] for item in self.data]
        self.tfidf_matrix = self.vectorizer.fit_transform(self.questions)

    def _load_data(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_best_match(self, query):
        """
        Returns the answer and confidence score.
        """
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        best_idx = similarities.argmax()
        score = similarities[best_idx]

        if score > 0.3:
            return self.data[best_idx]['answer']
        return None
