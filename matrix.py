
class Matrix:

    def __init__(self, entries = None):
        if entries is None:
            self.entries = []
            self.c = 0
            self.r = 0
        elif type(entries) == list:
            isValid = self.is_valid(entries)
            if not isValid:
                raise ValueError("Invalid Matrix input, please try again")
            else:
                self.entries = entries
                self.r, self.c = self.get_size(entries)
                if self.r == 1 and type(self.entries[0]) is int:
                    self.entries = [self.entries]
        
        else:
            raise TypeError("Expected type list, got type: "+str(type(entries)))
    
    def is_valid(self, entries):
        """Returns if a matrix is valid or not"""
        for i in range(1, len(entries)):
            if type(entries[i]) != type(entries[i-1]):
                return False
            elif type(entries[i]) == list and type(entries[i-1]) == list:
                if len(entries[i]) != len(entries[i-1]):
                    return False
        return True
    
    def get_size(self, entries):
        """
        Input: a valid matrix
        Returns: (r, c) of matrix
        """
        if not entries:
            return 0, 0
        type0 = type(entries[0])
        if type0 == int or type0 == float:
            return 1, len(entries)
        if type0 == list:
            return len(entries[0]), len(entries)

    def add_row(self, row):
        if type(row) != list:
            raise TypeError("Expected type list, got type: "+str(type(row)))
        else:
            if len(row) != self.c:
                raise ValueError("Expected row length: "+str(self.c)+", got: "+str(len(row)))
            else:
                self.entries.append(row)
                self.r += 1
    def add_column(self, col):
        if type(col) != list:
            raise TypeError("Expected type list, got type: "+str(type(row)))
        else:
            if len(col) != self.r:
                raise ValueError("Expected column length: "+str(self.r)+", got: "+str(len(col)))
            else:
                for i in range(self.r):
                    self.entries[i].append(col[i])
                self.c += 1

    ##Dunders/Important Matrix Operations

    def size(self):
        return self.r, self.c
    
    def __str__(self):
        if not self.entries:
            return 'Matrix: Empty'
        return 'Matrix: '+'\n\t'.join('|'+str(row)[1:-1]+'|' for row in self.entries)

    def __iter__(self):
        for row in self.entries:
            yield row
    
    def __copy__(self):
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
            raise ValueError("Sizes of matrices don't match")
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
            raise ValueError("Sizes of matrices don't match")
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
        

    def __pow__(self, exponent):
        """
        Returns: M_a ** exponent as new instance
        """
        pass
    
    def __iadd__(self, other):
        """
        Sets: M = M + other
        """
        pass
    
    def __isub__(self, other):
        """
        Sets: M = M + other
        """
        pass
    
    def __imul__(self, other):
        """
        Sets: M = M * other
        """
        pass

    def __ipow__(self, exponent):
        """
        Sets: M = M ** exponent
        """
        pass
    
    def transpose(self):
        """
        Returns the transpose of the matrix as a new instance of Matrix
        """
        pass
    
    

        


    

m = Matrix([[1,2,3], [4,5,6], [7, 8, 9]])
m1 = Matrix([[1,2,3], [4,5,6], [7,8,9]])
print(m - m1)