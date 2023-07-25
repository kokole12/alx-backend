#!/usr/bin/env python3
"""LIFO cache in python"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """initialising from the parent class"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """adding item to lifo cache"""
        if key is None or item is None:
            pass
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            key_last, value_last = self.cache_data.popitem()
            # self.cache_data.popitem()
            print("DISCARD: {}".format(key_last))
        self.cache_data[key] = item

    def get(self, key):
        """getting item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
