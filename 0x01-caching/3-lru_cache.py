#!/usr/bin/python3
""" Implementation of a LRU algorithm caching system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """"""
    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru = next(iter(self.cache_data))
                self.cache_data.pop(lru)
                print('DISCARD: {}'.format(lru))

    def get(self, key):
        """Get an item by key from the cache"""
        if key is not None:
            return self.cache_data.get(key)
        return None
