#!/usr/bin/env python3
"""LIFO cache in python"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """initialising from the parent class"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """adding item to lifo cache"""
        if key is None or item is None:
            pass
        length = len(self.cache_data)
        if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            print("DISCARD: {}".format(self.order[-1]))
            del self.cache_data[self.order[-1]]
            del self.order[-1]
        if key in self.order:
            del self.order[self.order.index(key)]
        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """getting item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
