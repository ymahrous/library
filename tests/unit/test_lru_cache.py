from app.infrastructure.cache.lru_cache import LRUCache

def test_lru_cache_put_and_get():
    cache = LRUCache(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)

    assert cache.get("a") == 1
    assert cache.get("b") == 2

def test_lru_eviction():
    cache = LRUCache(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)

    assert cache.get("a") is None
    assert cache.get("b") == 2
    assert cache.get("c") == 3