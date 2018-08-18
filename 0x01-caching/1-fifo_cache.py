#!/usr/bin/python3
"""
basic cache class
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ fifo cache class """
    def __init__(self):
        """ init """
        super().__init__()
        self.indx = []

    def put(self, key, item):
        """ to add items in cache """
        if key and item:
            self.cache_data[key] = item
            self.indx.append(key)
            if len(self.indx) > BaseCaching.MAX_ITEMS:
                key1 = self.indx.pop(0)
                print("DISCARD: {}".format(key1))
                del self.cache_data[key1]

    def get(self, key):
        """ to get items from cache """
        if key is not None:
            return self.cache_data.get(key)
