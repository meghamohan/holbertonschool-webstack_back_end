#!/usr/bin/python3
"""
mru class
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU cache class """
    def __init__(self):
        """ init """
        super().__init__()
        self.recnt = None

    def put(self, key, item):
        """ to add items in cache """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.recnt))
                del self.cache_data[self.recnt]
            self.cache_data[key] = item
            self.recnt = key

    def get(self, key):
        """ to get items from cache """
        returnVal = self.cache_data.get(key)
        if key is not None and returnVal:
            self.last_used = key
        return returnVal
