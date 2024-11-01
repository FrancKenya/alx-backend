#!/usr/bin/env python3
"""A program that contains a LFUCache class and displays the
implementation of the LFU algorithm"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ A class that shows the use of LFU as an algorithm to cache data"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache using LFU policy """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)
            self.frequency[key] += 1
        else:
            # Set initial frequency to 1 if it's a new item
            self.frequency[key] = 1

        # Add the item as the most recent
        self.cache_data[key] = item

        # If cache exceeds MAX_ITEMS, remove the least frequently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Find the least frequently used keys
            min_freq = min(self.frequency.values())
            least_frequent_keys = [
                k for k, freq in self.frequency.items() if freq == min_freq]

            if len(least_frequent_keys) > 1:
                for k in self.cache_data:
                    if k in least_frequent_keys:
                        lfu_key = k
                        break
            else:
                lfu_key = least_frequent_keys[0]

            self.cache_data.pop(lfu_key)
            del self.frequency[lfu_key]
            print("DISCARD:", lfu_key)

    def get(self, key):
        """ Get an item by key from the cache"""
        if key is not None:
            return self.cache_data.get(key)
        return None
