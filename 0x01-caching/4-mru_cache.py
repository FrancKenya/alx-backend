#!/usr/bin/env python3
""" A program that contains a MRUCache class
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ A class that displays the implementatiion of the MRU algorithm
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache after removing the most recently used item
        """
        if key is not None and item is not None:
            self.cache_data.pop(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_item = next(reversed(self.cache_data))
            del self.cache_data[mru_item]
            print('DISCARD: {}'.format(mru_item))

    def get(self, key):
        """ Get an item by key from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
