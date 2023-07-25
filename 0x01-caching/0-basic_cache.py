#!/usr/bin/env python3
"""basic cache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """initializing from super class"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assigning value to key"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """getting the value by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
