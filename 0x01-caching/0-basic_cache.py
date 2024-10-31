#!/usr/bin/env python3
"""This program contains a Child class that inherits from
the imported BaseCaching class"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class that inherits from BaseCaching and implements
    a caching system using dictionaries as a basic
    caching system"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """Put an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Used to get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
