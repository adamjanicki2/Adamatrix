import operations as op

class MatrixError(Exception):
    pass

class Matrix:

    def __init__(self, entries = None):
        if not entries:
            self.entries = []
            self.c = 0
            self.r = 0
        elif type(entries) == list:
            self.entries = entries
            if type(entries[0]) == int or type(entries[0]) == float:
                self.r, self.c = 1, len(entries)
            if type(entries[0]) == list:
                self.r, self.c = len(entries[0]), len(entries)
            if self.r == 1 and type(self.entries[0]) is int:
                self.entries = [self.entries]
        else:
            raise TypeError("Expected type list, got type: "+str(type(entries)))

    def row(self, index):
        if index >= self.c:
            raise IndexError
        return [element for element in self.entries[index]]
         
    def column(self, index):
        if index >= self.r:
            raise IndexError
        return [element[index] for element in self]

    def size(self):
        return self.r, self.c
    
    def __list__(self):
        return self.entries

    def __eq__(self, other):
        if self.size() != other.size():
            return False
        for row_a, row_b in zip(self, other):
            for entry_a, entry_b in zip(row_a, row_b):
                if entry_b != entry_a:
                    return False
        return True

    def __str__(self):
        if not self.entries:
            return 'Matrix: Empty'
        return 'Matrix: '+'\n\t'.join('|'+str(row)[1:-1]+'|' for row in self.entries)

    def __iter__(self):
        for row in self.entries:
            yield row

    def copy(self):
        """
        Returns copy of matrix as new instance
        """
        return Matrix(self.entries)
    
    def __setitem__(self, key, value):
        """
        Sets entry at spot (i, j) = value
        """
        if type(key) is tuple and len(key) == 2:
            if type(key[0]) is int and type(key[1]) is int:
                if key[0] < self.r and key[1] < self.c:
                    if type(value) is int or type(value) is float:
                        self.entries[key[0]][key[1]] = value
                    else:
                        raise ValueError("Type not supported, expected int or float")
                else:
                    raise IndexError("Indices out of bound for matrix")

        raise KeyError('Key of this type not supported')

    def __getitem__(self, key):
        """
        Returns entry at spot (i, j)
        """
        if type(key) is tuple and len(key) == 2:
            if type(key[0]) is int and type(key[1]) is int:
                if key[0] < self.r and key[1] < self.c:
                    return self.entries[key[0]][key[1]]

                else:
                    raise IndexError("Indices out of bound for matrix")

        raise KeyError('Key of this type not supported')

    def __add__(self, other):
        """
        Returns: M_a + M_b as new instance
        """
        if self.size() != other.size():
            raise MatrixError("Sizes of matrices don't match")
        new_entries = []
        for row_a, row_b in zip(self, other):
            new_row = []
            for entry_a, entry_b in zip(row_a, row_b):
                new_row.append(entry_a + entry_b)
            new_entries.append(new_row)
        return Matrix(new_entries)
    
    def __sub__(self, other):
        """
        Returns: M_a - M_b as new instance
        """
        if self.size() != other.size():
            raise MatrixError("Sizes of matrices don't match")
        new_entries = []
        for row_a, row_b in zip(self, other):
            new_row = []
            for entry_a, entry_b in zip(row_a, row_b):
                new_row.append(entry_a - entry_b)
            new_entries.append(new_row)
        return Matrix(new_entries)

    def __mul__(self, other):
        """
        Returns: M_a * M_b as new instance
        """
        return Matrix(op.mult_mat(list(self), list(other)))
            
    def __pow__(self, exponent):
        """
        Returns: M_a ** exponent as new instance
        """
        m = self.copy()
        for i in range(exponent-1):
            m *= self.copy()
        return m
    
    def __iadd__(self, other):
        """
        Sets: M = M + other
        """
        return self + other
    
    def __isub__(self, other):
        """
        Sets: M = M + other
        """
        return self - other
    
    def __imul__(self, other):
        """
        Sets: M = M * other
        """
        return self * other

    def __ipow__(self, exponent):
        """
        Sets: M = M ** exponent
        """
        return self ** exponent
    
    def transpose(self):
        """
        Returns the transpose of the matrix as a new instance of Matrix
        """
        o = []
        for i in range(self.r):
            o.append(self.column(i))
        return Matrix(o)

    def eliminate(self):
        """
        Returns new matrix that is the upper triangular form of
        """
        return op.upper_triangular(list(self))

    def det(self):
        """
        Calculates determinant of matrix
        """
        if self.c != self.r:
            raise MatrixError("Non-square matrices do not have determinants")
        return op.det(list(self))