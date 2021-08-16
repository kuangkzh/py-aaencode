import random


class OptionDict(dict):
    def __setitem__(self, key, value):
        if isinstance(value, list):
            super(OptionDict, self).__setitem__(key, value)
        elif self.__contains__(key):
            self[key].append(value)
        else:
            super(OptionDict, self).__setitem__(key, [value])

    def __getitem__(self, k):
        res = super(OptionDict, self).__getitem__(k)
        return res[random.randrange(len(res))]
