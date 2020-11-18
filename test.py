from matrix import Matrix
import numpy as np
import unittest
import random
import operations as op

def test_mul(array_a, array_b):
    expected = np.matmul(array_a, array_b).tolist()
    received = Matrix(array_a) * Matrix(array_b)
    return expected == list(received)

def test_sub(a, b):
    expected = np.subtract(a, b).tolist()
    received = Matrix(a) - Matrix(b)
    return expected == list(received)

def test_add(a, b):
    expected = np.add(a, b).tolist()
    received = Matrix(a) + Matrix(b)
    return expected == list(received)

def test_transpose(a):
    expected = np.transpose(a).tolist()
    received = list(Matrix(a).transpose())
    return expected == received

def test_power(a, exponent):
    expected = np.linalg.matrix_power(a, exponent).tolist()
    received = list(Matrix(a) ** exponent)
    return received == expected

class TestCases(unittest.TestCase):

    def test_add_01(self):
        A = [[random.randint(1, 20) for j in range(10)] for i in range(10)]
        B = [[random.randint(1, 20) for j in range(10)] for i in range(10)]
        self.assertEqual(test_add(A, B), True)
    def test_add_02(self):
        A = [[random.randint(1, 20) for j in range(9)] for i in range(10)]
        B = [[random.randint(1, 20) for j in range(10)] for i in range(10)]
        try:
            test_add(A, B)
        except:
            self.assertEqual(True, True)
        else:
            self.assertEqual(False, True)
    def test_mul_03(self): 
        I = [[1,0,0], [0, 1, 0], [0,0,1]]
        A = [[1,2,3], [1,2,3], [1,2,3]]
        self.assertEqual(test_mul(A, A), True)

    def test_mul_04(self): 
        A = [[random.randint(1, 20) for j in range(10)] for i in range(10)]
        B = [[random.randint(1, 20) for j in range(10)] for i in range(10)]
        res_1 = test_mul(A, B)
        res_2 = test_mul(B, A)
        self.assertEqual(res_1 and res_2, True)

    def test_mul_05(self): 
        A = [[random.randint(1, 20) for j in range(10)] for i in range(8)]
        B = [[random.randint(1, 20) for j in range(8)] for i in range(10)]
        res_1 = test_mul(A, B)
        self.assertEqual(res_1, True)

    def test_mul_06(self): 
        A = [[random.randint(1, 20) for j in range(10)] for i in range(10)]
        B = [[random.randint(1, 20) for j in range(5)] for i in range(5)]
        try:
            res_1 = test_mul(A, B)
            res_2 = test_mul(B, A)
            self.assertEqual(False, True)
            print("Error should have been raised")
        except:
            self.assertEqual(True, True)
        
    def test_mul_07(self): 
        A = [[random.randint(1, 20) for j in range(10)] for i in range(15)]
        B = [[random.randint(1, 20) for j in range(17)] for i in range(19)]
        try:
            res_1 = test_mul(A, B)
            res_2 = test_mul(B, A)
            self.assertEqual(False, True)
            print("Error should have been raised")
        except:
            self.assertEqual(True, True)
    
    def test_transpose_08(self):
        A = [[random.randint(1, 100) for j in range(20)] for i in range(10)]
        self.assertEqual(test_transpose(A), True)
    
    def test_transpose_09(self):
        A = [[random.randint(1, 100) for j in range(10)] for i in range(15)]
        self.assertEqual(test_transpose(A), True)

    def test_power_10(self):
        A = [[random.randint(1, 10) for j in range(10)] for i in range(10)]
        self.assertEqual(test_power(A, random.randint(5,10)), True)

    

       

if __name__ == '__main__':
    res = unittest.main(verbosity = 3, exit = False)