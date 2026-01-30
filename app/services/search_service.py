class SearchService:
    def __init__(self, repository, cache):
        self.repo = repository
        self.cache = cache

    def search(self, **filters):
        key = tuple(sorted(filters.items()))
        cached = self.cache.get(key)
        if cached is not None:
            return cached

        results = self.repo.search_books(**filters)
        self.cache.put(key, results)
        return results