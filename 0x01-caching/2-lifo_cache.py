#!/usr/bin/env python3
""" A program that contains a LIFOCache class
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A class that displays the use of LIFO algorithm to
    cache data
    """
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Use LIFO to remove an item and add a new one"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.last_key = key
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last_key]
            print('DISCARD: {}'.format(self.last_key))

    def get(self, key):
        """Get an item by key from the cache"""
        if key is not None:
            return self.cache_data.get(key)
        return None
