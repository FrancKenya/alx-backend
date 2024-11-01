#!/usr/bin/env python3
"""A program that contains an LFUCache class and displays the
implementation of the LFU algorithm"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """A class that implements LFU caching policy"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = {}

    def put(self, key, item):
        """Add an item to the cache using LFU policy with LRU tie-breaking"""
        if key is None or item is None:
            return

        # If key exists, update its position and increase frequency
        if key in self.cache_data:
            self.cache_data.pop(key)
            self.frequency[key] += 1
        else:
            # Set frequency to 1 for new item
            self.frequency[key] = 1

        # Add the item as the most recent in OrderedDict
        self.cache_data[key] = item

        # If cache exceeds MAX_ITEMS, remove the least frequently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Find the minimum frequency
            min_freq = min(self.frequency.values())

            # Filter the keys with the minimum frequency
            least_frequent_keys = [
                k for k in self.cache_data if self.frequency[k] == min_freq]

            # Apply LRU: select the first item from the left in OrderedDict
            lfu_key = least_frequent_keys[0]

            # Remove the selected key
            self.cache_data.pop(lfu_key)
            del self.frequency[lfu_key]
            print("DISCARD:", lfu_key)

    def get(self, key):
        """Retrieve an item from the cache and update its frequency"""
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency of the key as it has been accessed
        self.frequency[key] += 1

        # Move accessed item to the end of OrderedDict to mark it as recent
        self.cache_data.move_to_end(key)

        return self.cache_data[key]
