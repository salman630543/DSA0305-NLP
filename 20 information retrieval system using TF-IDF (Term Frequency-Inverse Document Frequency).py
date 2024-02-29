import math
from collections import Counter

class TFIDF:
    def __init__(self, documents):
        self.documents = documents
        self.tf_scores = []
        self.idf_scores = {}
        self.tfidf_scores = []

    def calculate_tf(self, document):
        tf_score = Counter(document)
        for key in tf_score:
            tf_score[key] = tf_score[key] / float(len(document))
        return tf_score

    def calculate_idf(self):
        total_documents = len(self.documents)
        idf_scores = {}
        all_words_set = self.get_all_words()

        for word in all_words_set:
            count = 0
            for document in self.documents:
                if word in document:
                    count += 1
            idf_scores[word] = math.log10(total_documents / float(count))

        return idf_scores

    def calculate_tfidf(self):
        idf_scores = self.calculate_idf()
        for document in self.documents:
            tf_score = self.calculate_tf(document)
            tfidf_score = {}
            for word in tf_score:
                tfidf_score[word] = tf_score[word] * idf_scores[word]
            self.tfidf_scores.append(tfidf_score)

    def get_all_words(self):
        all_words_set = set()
        for document in self.documents:
            all_words_set |= set(document)
        return all_words_set

    def rank_documents(self, query):
        query_words = query.split()
        query_tf_score = self.calculate_tf(query_words)

        for idx, document in enumerate(self.documents):
            document_score = 0
            for word in query_words:
                if word in self.tfidf_scores[idx]:
                    document_score += self.tfidf_scores[idx][word] * query_tf_score[word]
            self.tf_scores.append((idx, document_score))

        ranked_documents = sorted(self.tf_scores, key=lambda x: x[1], reverse=True)
        return ranked_documents


if __name__ == "__main__":
    # Sample documents
    documents = [
        ["this", "is", "a", "sample", "document", "one"],
        ["this", "is", "another", "example", "document", "two"],
        ["yet", "another", "document", "three", "example"]
    ]

    # Initialize the TFIDF class
    tfidf = TFIDF(documents)
    tfidf.calculate_tfidf()

    # Sample query
    query = "example document"

    # Rank documents based on the query
    ranked_documents = tfidf.rank_documents(query)

    # Display the ranked documents
    for idx, score in ranked_documents:
        print(f"Document {idx + 1}: Score {score}")
