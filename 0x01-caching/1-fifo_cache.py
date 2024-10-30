#!/usr/bin/env python3
""" 1-fifo_cache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""
    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """Discards the first item  in the cache and adds
        a new one
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[0]
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """Get an item by key from the cache"""
        if key is not None:
            return self.cache_data.get(key)
        return None
