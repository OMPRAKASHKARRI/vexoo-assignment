from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class KnowledgeNode:
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.summary = self.summarize(raw_text)
        self.category = self.classify(raw_text)
        self.keywords = self.extract_keywords(raw_text)

    def summarize(self, text):
        return text[:150]  # placeholder summary

    def classify(self, text):
        text = text.lower()
        if any(word in text for word in ["error", "fail", "bug"]):
            return "technical"
        elif any(word in text for word in ["data", "model", "ai"]):
            return "ai"
        return "general"

    def extract_keywords(self, text):
        words = text.split()
        return list(set(words[:10]))


class KnowledgeBase:
    def __init__(self):
        self.nodes = []
        self.vectorizer = TfidfVectorizer()
        self.vectors = None

    def add_documents(self, chunks):
        for chunk in chunks:
            self.nodes.append(KnowledgeNode(chunk))

        summaries = [node.summary for node in self.nodes]
        self.vectors = self.vectorizer.fit_transform(summaries)

    def search(self, query):
        query_vec = self.vectorizer.transform([query])
        scores = np.dot(self.vectors, query_vec.T).toarray()

        best_idx = np.argmax(scores)
        return self.nodes[best_idx]


def sliding_window(text, window_size=500, overlap=100):
    chunks = []
    for i in range(0, len(text), window_size - overlap):
        chunks.append(text[i:i+window_size])
    return chunks