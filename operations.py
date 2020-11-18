def dot(c, r):
    """
    dots two vectors c and r
    """
    if len(c) != len(r):
        raise ValueError('Vector lengths not equal')
    total = 0
    for i, j in zip(c, r):
        total += i*j
    return total

def mult_mat(m1, m2):
    """
    multiplies two matrices m1, m2, 2D lists
    """
    if len(m1[0]) != len(m2):
        raise ValueError('Matrices do not have correct sizes to be multiplied')
    rows_a = m1
    cols_b = [[row[i] for row in m2] for i in range(len(m2[0]))]
    out = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]
    for row in range(len(out)):
        for col in range(len(out[0])):
            out[row][col] = dot(rows_a[row], cols_b[col])
    return out

def upper_triangular(A):
    m = A.copy()
    for i in range(min(len(m), len(m[0]))):
        for j in range(i+1, min(len(m), len(m[0]))):
            scalar = 0 if m[i][i] == 0 else float(m[j][i] / m[i][i]) ##ratio with pivot
            for k in range(len(m[0])):
                m[j][k] -= scalar * m[i][k]
    return m

def det(A):
    u = upper_triangular(A)
    out = 1
    for i in range(len(u)):
        out *= u[i][i]
    return 0 if out == 0.0 or out == -0.0 else out

def lsq(A, b):
    """
    Solves least squares for Ax = b
    """
    raise NotImplementedError

def back_sub(augmented):
    """
    Solves by back substituting
    """
    out = [0 for _ in augmented]
    for i in range(len(augmented) - 1, -1, -1):
        summed = sum([out[idx]*augmented[i][idx] for idx in range(len(augmented[0]) - 1)])
        out[i] = float((augmented[i][-1] - summed) / augmented[i][i])
    return out

