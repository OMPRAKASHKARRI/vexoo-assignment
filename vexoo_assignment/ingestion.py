from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


class KnowledgeNode:
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.summary = self.summarize(raw_text)
        self.category = self.classify(raw_text)
        self.keywords = self.extract_keywords(raw_text)

    def summarize(self, text):
        return text[:150]

    def classify(self, text):
        text = text.lower()
        if any(word in text for word in ["error", "bug", "fail"]):
            return "technical"
        elif any(word in text for word in ["ai", "machine", "learning"]):
            return "ai"
        elif any(word in text for word in ["system", "os", "operating"]):
            return "system"
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
        scores = (self.vectors @ query_vec.T).toarray()

        best_score = 0
        best_node = None

        for i, node in enumerate(self.nodes):
            score = scores[i][0]

            # Boost: raw text match
            if query.lower() in node.raw_text.lower():
                score += 0.3

            # Boost: keyword match
            if any(word.lower() in [k.lower() for k in node.keywords] for word in query.split()):
                score += 0.2

            # Boost: category match
            if node.category in query.lower():
                score += 0.1

            if score > best_score:
                best_score = score
                best_node = node

        return best_node


def sliding_window(text, window_size=300, overlap=50):
    chunks = []
    for i in range(0, len(text), window_size - overlap):
        chunks.append(text[i:i + window_size])
    return chunks