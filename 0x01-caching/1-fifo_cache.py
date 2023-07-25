#!/usr/bin/env python3
"""fifo caching to del first item in the dictionary"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """initialzing from super class"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """addding to fifo queue"""
        if key is None or item is None:
            pass
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
            and key not in self.cache_data.keys():
            key_first = next(iter(self.cache_data.keys()))
            del self.cache_data[key_first]
            print("DISCARD: {}".format(key_first))
        self.cache_data[key] = item

    def get(self, key):
        """getting item by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
