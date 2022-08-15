import unittest
from main import Matrice
from .exception import SizeMismatchError


class MatriceTestRunner(unittest.TestCase):

    # __add__ tests
    def test_additions(self):
        a = Matrice([[1,2],
                     [3,4]])       
        b = Matrice([[1,2],
                     [3,4]])
        c = Matrice([[2,4],
                     [6,8]])

        self.assertEqual(a + b, c, "Matrice addition failed.")

        e = Matrice([[2,3]])

        self.assertRaises(SizeMismatchError, lambda: a + e)

    # __sub__ tests
    def test_subtractions(self):
        a = Matrice([[1,2],
                     [3,4]])
        b = Matrice([[1,2],
                     [3,4]])
        c = Matrice([[0,0],
                     [0,0]])

        self.assertEqual(a - b, c, "Matrice subtraction failed.")

        e = Matrice([[2,3]])

        self.assertRaises(SizeMismatchError, lambda: a - e)

    # __mul__ tests
    def test_multiplications(self):
        a = Matrice([[1,2],
                     [3,4]])
        b = Matrice([[1,2],
                     [3,4]])
        c = Matrice([[1,4],
                     [9,16]])

        self.assertEqual(a * b, c, "Matrice multiplication of 2 matrices failed.")

        d = Matrice([[2,4],
                     [6,8]])
        
        self.assertEqual(a*2, d, "Matrice multiplication with a scalar constant failed.")

        e = Matrice([[2,3,4]])

        self.assertRaises(TypeError, lambda: a * e)

    # __truediv__ tests
    def test_division(self):
        a = Matrice([[1,2],
                     [3,4]])
        b = Matrice([[1,2],
                     [3,4]])
        c = Matrice([[1.0,1.0],
                     [1.0,1.0]])

        self.assertEqual(a / b, c, "Matrice division of 2 matrices failed.")

        d = Matrice([[.5,1.0],
                     [1.5,2.0]])
        
        self.assertEqual(a/2, d, "Matrice divisoin with a scalar constant failed.")

        e = Matrice([[2,3,4]])

        self.assertRaises(TypeError, lambda: a / e)

    
    # __eq__ tests
    def test_equal(self):
        a = Matrice([[1,2],
                     [3,4]])
        b = Matrice([[1,2],
                     [3,4]])
        c = Matrice([[1.0,1.0],
                     [1.0,1.0]])

        d = Matrice([[1,2,3]])

        self.assertEqual(a == b, True, "Matrice comparison of 2 matrices failed.")
        self.assertEqual(a == c, False, "Matrice comparison of 2 matrices with same shape but different values failed.")
        self.assertEqual(a == d, False, "Matrice comparison of 2 matrices with different shape failed.")

    # .column(y) tests
    def test_column(self):
        a = Matrice([[1,2],
                     [3,4]]) 

        self.assertEqual(a.column(0), [1,3], "Matrice.column(0) failed.")
        self.assertEqual(a.column(1), [2,4], "Matrice.column(1) failed.")

    # .flatten() test
    def test_column(self):
        a = Matrice([[1,2],
                     [3,4]]) 

        self.assertEqual(a.flatten(), [1,2,3,4], "Matrice.flatten() failed.")

    # .T() test (Transpose test)
    def test_transpose(self):
        a = Matrice([[1,2,3],
                     [4,5,6]])
        b = Matrice([[1,4],
                     [2,5],
                     [3,6]])

        self.assertEqual(a.T(), b, "Matrice.T() [Transpose function] failed.")
            
        
    # .multiply(other) test (Matrice multiplication)
    def test_matriceMultiplication(self):
        a = Matrice([[1,2,3],
                     [4,5,6]])
        b = Matrice([[1,2],
                     [3,4],
                     [5,6]])
        d = Matrice([[22,28],
                     [49,64]])
                     
        self.assertEqual(a.multiply(b), d, "Matrice multiplication failed.")
        # Errors        
        self.assertRaises(TypeError, lambda: a.multiply(2))
        
        e = Matrice([[1,2,3],
                     [4,5,6]])

        self.assertRaises(SizeMismatchError, lambda: a.multiply(e))
    

if __name__ == "__main__":
    unittest.main()