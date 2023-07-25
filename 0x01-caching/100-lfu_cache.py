#!/usr/bin/env python3
"""
    Create a class LFUCache that inherits from
    BaseCaching and is a caching system
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
        if length >= BaseCaching.MAX_ITEMS and\
                key not in self.cache_data.keys():
            item_del = next(iter(self.cache_data.keys()))
            print("Discard: {}".format(item_del))
            del item_del
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """returning item at key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
