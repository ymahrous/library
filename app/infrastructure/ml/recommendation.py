from collections import Counter

class RecommendationSystem:
    def __init__(self, user_history, books):
        self.user_history = user_history
        self.books = books

    def recommend(self, user_id, limit=3):
        if user_id not in self.user_history:
            return []

        seen = set(self.user_history[user_id])
        scores = Counter()

        for user, history in self.user_history.items():
            if user == user_id:
                continue
            overlap = seen & set(history)
            for book_id in history:
                if book_id not in seen:
                    scores[book_id] += len(overlap)

        return [self.books[b].title for b, _ in scores.most_common(limit)]