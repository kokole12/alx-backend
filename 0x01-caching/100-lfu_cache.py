#!/usr/bin/env python3
"""
    Create a class LFUCache that inherits from BaseCaching and is a caching system:
    You must use self.cache_data - dictionary from the parent class BaseCaching
    You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
    def put(self, key, item):
       Must assign to the dictionary self.cache_data the item value for the key key.
       If key or item is None, this method should not do anything.
       If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
    you must discard the least frequency used item (LFU algorithm)
       if you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used
       you must print DISCARD: with the key discarded and following by a new line
    def get(self, key):
       Must return the value in self.cache_data linked to key.
       If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """decletring the class methods"""

    def __init__(self):
        """initializing values for defaults"""
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """adding items to the cache"""
        length = len(self.cache_data)
        if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data.keys():
            item_del =  next(iter(self.cache_data.keys()))
            print("Discard: {}".format(item_del))
            del item_del
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
