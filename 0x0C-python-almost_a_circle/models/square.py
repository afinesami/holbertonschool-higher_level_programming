#.rectangle import Rectangle


class Square(Rectangle):
    """Square Class Reclangle
"""
    def __init__(self, size, x=0, y=0, id=None):
        """method : init magic 
"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method : str magic 
"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """method : size getter
"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """method : update
"""
        if len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """method : to_dictionary
"""
        n_dictionar = {}
        n_dictionar["id"] = self.id
        n_dictionar["size"] = self.size
        n_dictionar["x"] = self.x
        n_dictionar["y"] = self.y
        return n_dictionar
