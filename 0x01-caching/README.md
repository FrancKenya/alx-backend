Caching System Project
This project is a collection of caching system implementations in Python. Each caching class applies a specific caching policy to manage and evict items from the cache when it exceeds a maximum limit. The project covers caching algorithms such as FIFO, LIFO, LRU, MRU, and LFU.

Project Structure
All code is written for Python 3.7 and follows pycodestyle standards.
Each caching class inherits from the BaseCaching parent class, which provides core caching functionality and a limit on cache size.
Documentation is included for each module, class, and function as required.
Getting Started
Requirements
Python Version: 3.7
OS: Ubuntu 18.04 LTS
Style Guide: Code follows pycodestyle style (version 2.5).
Files
base_caching.py: Defines the BaseCaching class, which provides the base cache structure, a limit (MAX_ITEMS set to 4), and methods to be overridden by subclasses.
README.md: This file.
Caching Classes:
BasicCache: Basic cache with no limit.
FIFOCache: Cache with FIFO eviction.
LIFOCache: Cache with LIFO eviction.
LRUCache: Cache with LRU eviction.
MRUCache: Cache with MRU eviction.
LFUCache: Cache with LFU eviction.
Caching Algorithms
Each caching class implements one of the following algorithms:

FIFO (First-In, First-Out): Discards the oldest entry when the cache limit is reached. This policy is implemented in FIFOCache.
LIFO (Last-In, First-Out): Discards the most recently added item when the cache limit is exceeded. This policy is implemented in LIFOCache.
LRU (Least Recently Used): Discards the least recently accessed item when the cache limit is reached. This policy is implemented in LRUCache.
MRU (Most Recently Used): Discards the most recently accessed item when the cache limit is reached. This policy is implemented in MRUCache.
LFU (Least Frequently Used): Discards the least frequently accessed item when the cache limit is reached. If multiple items have the same frequency, it discards the least recently used of those items. This policy is implemented in LFUCache.
Usage and Examples
BaseCaching Class
The BaseCaching class serves as the foundation for all caching classes. It defines:

MAX_ITEMS (set to 4): The maximum number of items allowed in the cache.
cache_data: A dictionary to store cached items.
put(key, item): An abstract method for adding items to the cache, implemented in subclasses.
get(key): An abstract method for retrieving items from the cache, implemented in subclasses.

Class-Specific Details
BasicCache: No limit to the number of items stored; items are not evicted.
FIFOCache: Discards the oldest added item when the cache limit is reached.
LIFOCache: Discards the most recently added item when the cache limit is reached.
LRUCache: Discards the least recently accessed item upon reaching the cache limit.
MRUCache: Discards the most recently accessed item upon reaching the cache limit.
LFUCache: Discards the least frequently accessed item upon reaching the cache limit. If there's a tie in frequency, the LRU item is discarded.
Project Rules
Each file must be executable and end with a newline.
Files will be tested with wc to ensure proper length.
Each module, class, and function has accompanying documentation.
In each caching class, methods put() and get() must handle None keys and values gracefully, i.e., they do not perform any operation when key or item is None.

Testing
It is done through the main files provided for every task
