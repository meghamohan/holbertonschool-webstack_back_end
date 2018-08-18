#!/usr/bin/python3
"""
basic cache class
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ basic cache class """
    def put(self, key, item):
        """ to add items in cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ to get items from cache """
        if key is not None:
            return self.cache_data.get(key)
