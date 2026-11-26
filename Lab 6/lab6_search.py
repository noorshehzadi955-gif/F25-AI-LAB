from sklearn.feature_extraction.text import TfidfVectorizer


class Retriever:
    def __init__(self, records):
        if not records:
            raise ValueError("Please provide FAQ records.")

        self.records = records
        texts = [record["text"] for record in records]

        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform(texts)

    def search(self, query, k=3):
        if not query.strip():
            return []

        query_vector = self.vectorizer.transform([query])

        # No words in common with the FAQ list
        if query_vector.nnz == 0:
            return []

        scores = (query_vector @ self.matrix.T).toarray()[0]

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: (-scores[i], i)
        )

        results = []
        for i in ranked_indices[:k]:
            if scores[i] > 0:
                results.append((self.records[i], float(scores[i])))

        return results
