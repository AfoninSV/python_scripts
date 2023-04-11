"""
A class MyDict that behaves like a regular dictionary, but the get method returns 0 by default instead of None.
"""

class MyDict(dict):
    def get(self, key):
        return_value = super().get(key)
        if return_value is None:
            return 0
        return return_value
