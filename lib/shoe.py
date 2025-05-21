#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size: int, condition = ""):
        self.brand = brand
        self.size = size
        self.condition = condition

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")