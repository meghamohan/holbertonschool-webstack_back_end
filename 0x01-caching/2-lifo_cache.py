#!/usr/bin/python3
"""
lifo class
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ fifo cache class """
    def __init__(self):
        """ init """
        super().__init__()
        self.indx = []

    def put(self, key, item):
        """ to add items in cache """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                endKey = self.indx.pop()
                print("DISCARD: {}".format(endKey))
                del self.cache_data[endKey]
            self.indx.append(key)

    def get(self, key):
        """ to get items from cache """
        return self.cache_data.get(key)
