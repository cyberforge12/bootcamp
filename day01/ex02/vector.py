import numpy


class Vector:
    def __init__(self, num):
        if type(num) is int:
            self.length = num
            self.values = list(numpy.arange(0, 0 + num, 1.0))
        elif type(num) is list:
            self.values = num
            self.length = len(num)
        elif type(num) is tuple:
            self.values = list(numpy.arange(num[0], num[1], 1.0))
            self.length = len(self.values)
        else:
            raise ValueError('Provide a list of floats, a tuple with start and end values or vector length')

    # add : scalars and vectors, can have errors with vectors.
    def __add__(self, other):
        if type(other) in [int, float]:
            return [i + other for i in self.values]
        elif type(other) == Vector:
            elif len(other.values) == 1:
                return [i * other[0] for i in self.values]
            elif len(other.values) == len(self.values):
                return [a * b for a, b in zip(self.values, other.values)]
            else:
                raise ValueError('Incorrect multiplication.\n'
                                 '\tPlease provide:\n'
                                 '\t- two vectors of the same length, or\n'
                                 '\t- a vector and a scalar, or\n'
                                 '\t- a vector and vector of size one')
    elif len(other) == 1 and type(other[0]):
            return [i * other[0] for i in self.values]
        elif len(other) == len(self.values):
            return [a * b for a, b in zip(self.values, other)]
        else:
            raise ValueError('Incorrect multiplication.\n'
                             '\tPlease provide:\n'
                             '\t- two vectors of the same length, or\n'
                             '\t- a vector and a scalar, or\n'
                             '\t- a vector and vector of size one')
        return ret

    __radd__ = __add__

    # sub : scalars and vectors, can have errors with vectors.
    def __sub__(self, other):
        ret = list(self.values)
        for i in other:
            ret.remove(i)
        return ret

    def __rsub__(self, other):
        ret = list(other)
        for i in self.values:
            ret.remove(i)
        return ret

    # div : only scalars.
    def __truediv__(self, other):
        if len(self.values) == 1 and type(other) in [int, float]:
            return self.values[0] / other
        else:
            raise ValueError ("Incorrect division: can only divide two scalars")

    def __rtruediv__(self, other):
        if len(self.values) == 1 and type(other) in [int, float]:
            return other / self.values[0]
        else:
            raise ValueError ("Incorrect division: can only divide two scalars")

    # mul : scalars and vectors, can have errors with vectors,
    # return a scalar if we perform Vector * Vector (dot product)
    def __mul__(self, other):
        if type(other) in [int, float]:
            return [i * other for i in self.values]
        elif type(other) == Vector:
            return [a * b for a, b in zip(self.values, other.values)]
        elif len(other) == 1:
            return [i * other[0] for i in self.values]
        elif len(other) == len(self.values):
            return [a * b for a, b in zip(self.values, other)]
        else:
            raise ValueError('Incorrect multiplication.\n'
                             '\tPlease provide:\n'
                             '\t- two vectors of the same length, or\n'
                             '\t- a vector and a scalar, or\n'
                             '\t- a vector and vector of size one')

    __rmul__ = __mul__

    def __str__(self):
        return f"{[i for i in self.values]}"

    def __repr__(self):
        return f'Vector({self.values})'

