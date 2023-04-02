class MyDict(dict):
    def get(self, key):
        return_value = super().get(key)
        if return_value is None:
            return 0
        return return_value
