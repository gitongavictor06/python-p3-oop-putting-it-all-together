class Shoe:
    def __init__(self, brand, size, material):
        self.brand = brand
        self.size = size
        self.material = material
        self._condition = "New"
        self._repair_history = []

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise TypeError("Brand must be a string")
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be a positive integer")
        self._size = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        if not isinstance(value, str):
            raise TypeError("Material must be a string")
        self._material = value

    @property
    def condition(self):
        return self._condition

    def cobble(self):
        self._condition = "New"
        self._repair_history.append("cobbled")
        print("Your shoe is as good as new!")

    def wear(self):
        if self._condition == "New":
            self._condition = "Used"
        elif self._condition == "Used":
            self._condition = "Worn"
        elif self._condition == "Worn":
            self._condition = "Tattered"
        return self.condition

    def get_repair_history(self):
        return self._repair_history.copy()

    def __str__(self):
        return f"{self.brand} shoe (size {self.size}, {self.material})"

    def __repr__(self):
        return f"Shoe(brand='{self.brand}', size={self.size}, material='{self.material}')"