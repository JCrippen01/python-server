class Location():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, is_open):
        self.id = id
        self.name = name
        self.is_open = is_open
        