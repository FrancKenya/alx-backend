#!/usr/bin/env python3
""" A program that contains a LIFOCache class
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A class implementing LIFO caching policy"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.lifo_cache = []  # Tracks the order of insertion

    def put(self, key, item):
        """Add an item in the cache using LIFO policy"""
        if key is not None and item is not None:
            # Remove the key from LIFO order if it exists
            if key in self.lifo_cache:
                self.lifo_cache.remove(key)

            self.cache_data[key] = item
            self.lifo_cache.append(key)

            # If cache exceeds max size, discard the last item in LIFO order
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.lifo_cache.pop(-2)
                del self.cache_data[last_key]
                print('DISCARD: {}'.format(last_key))

    def get(self, key):
        """Get an item by key from the cache"""
        return self.cache_data.get(key) if key is not None else None
