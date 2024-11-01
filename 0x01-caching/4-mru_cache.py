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
        self.list_1 = []

    def put(self, key, item):
        """ Add an item in the cache after removing the most recently used item
        """
        if key is not None and item is not None:
            if len(self.list_1) == self.MAX_ITEMS:
                if key not in self.list_1:
                    leftmost = self.list_1.pop()
                    print("DISCARD: {}".format(leftmost))
                    del self.cache_data[leftmost]
                else:
                    self.list_1.remove(key)
            self.list_1.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key from the cache
        """
        if key is not None and key in self.list_1:
            self.list_1.remove(key)
            self.list_1.append(key)
            return self.cache_data.get(key)
        return None
