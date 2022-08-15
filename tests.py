import unittest
from main import Matrix
from exception import SizeMismatchError


class MatriceTestRunner(unittest.TestCase):

    # __add__ tests
    def test_additions(self):
        a = Matrix([[1,2],
                     [3,4]])       
        b = Matrix([[1,2],
                     [3,4]])
        c = Matrix([[2,4],
                     [6,8]])

        self.assertEqual(a + b, c, "Matrix addition failed.")

        e = Matrix([[2,3]])

        self.assertRaises(SizeMismatchError, lambda: a + e)

    # __sub__ tests
    def test_subtractions(self):
        a = Matrix([[1,2],
                     [3,4]])
        b = Matrix([[1,2],
                     [3,4]])
        c = Matrix([[0,0],
                     [0,0]])

        self.assertEqual(a - b, c, "Matrix subtraction failed.")

        e = Matrix([[2,3]])

        self.assertRaises(SizeMismatchError, lambda: a - e)

    # __mul__ tests
    def test_multiplications(self):
        a = Matrix([[1,2],
                     [3,4]])
        b = Matrix([[1,2],
                     [3,4]])
        c = Matrix([[1,4],
                     [9,16]])

        self.assertEqual(a * b, c, "Matrix multiplication of 2 matrices failed.")

        d = Matrix([[2,4],
                     [6,8]])
        
        self.assertEqual(a*2, d, "Matrix multiplication with a scalar constant failed.")

        e = Matrix([[2,3,4]])

        self.assertRaises(TypeError, lambda: a * e)

    # __truediv__ tests
    def test_division(self):
        a = Matrix([[1,2],
                     [3,4]])
        b = Matrix([[1,2],
                     [3,4]])
        c = Matrix([[1.0,1.0],
                     [1.0,1.0]])

        self.assertEqual(a / b, c, "Matrix division of 2 matrices failed.")

        d = Matrix([[.5,1.0],
                     [1.5,2.0]])
        
        self.assertEqual(a/2, d, "Matrix divisoin with a scalar constant failed.")

        e = Matrix([[2,3,4]])

        self.assertRaises(TypeError, lambda: a / e)

    
    # __eq__ tests
    def test_equal(self):
        a = Matrix([[1,2],
                     [3,4]])
        b = Matrix([[1,2],
                     [3,4]])
        c = Matrix([[1.0,1.0],
                     [1.0,1.0]])

        d = Matrix([[1,2,3]])

        self.assertEqual(a == b, True, "Matrix comparison of 2 matrices failed.")
        self.assertEqual(a == c, False, "Matrix comparison of 2 matrices with same shape but different values failed.")
        self.assertEqual(a == d, False, "Matrix comparison of 2 matrices with different shape failed.")

    # .column(y) tests
    def test_column(self):
        a = Matrix([[1,2],
                     [3,4]]) 

        self.assertEqual(a.column(0), [1,3], "Matrix.column(0) failed.")
        self.assertEqual(a.column(1), [2,4], "Matrix.column(1) failed.")

    # .flatten() test
    def test_column(self):
        a = Matrix([[1,2],
                     [3,4]]) 

        self.assertEqual(a.flatten(), [1,2,3,4], "Matrix.flatten() failed.")

    # .T() test (Transpose test)
    def test_transpose(self):
        a = Matrix([[1,2,3],
                     [4,5,6]])
        b = Matrix([[1,4],
                     [2,5],
                     [3,6]])

        self.assertEqual(a.T(), b, "Matrix.T() [Transpose function] failed.")
            
        
    # .multiply(other) test (Matrice multiplication)
    def test_matriceMultiplication(self):
        a = Matrix([[1,2,3],
                     [4,5,6]])
        b = Matrix([[1,2],
                     [3,4],
                     [5,6]])
        d = Matrix([[22,28],
                     [49,64]])
                     
        self.assertEqual(a.multiply(b), d, "Matrice multiplication failed.")
        # Errors        
        self.assertRaises(TypeError, lambda: a.multiply(2))
        
        e = Matrix([[1,2,3],
                     [4,5,6]])

        self.assertRaises(SizeMismatchError, lambda: a.multiply(e))
    

if __name__ == "__main__":
    unittest.main()