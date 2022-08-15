from exception import SizeMismatchError

class Matrix:
    def __init__(self, arr):
        # Store the raw arr
        self.matrix = arr

        # Store the shape of the vector
        self.x = len(arr)
        self.y = len(arr[0])

    
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        # Turn the vector into a string
        result = '-m'+str(self.matrix)+'m-'
        result = result.replace('-m[', 'Matrix(')
        result = result.replace(']m-', ')')
        result = result.replace(', [', '\n       [')

        return result
        
    # Get method, example array[x]
    def __getitem__(self, key):
        return self.matrix[key]

    # Add two matrice with it's corresponding element
    def __add__(self, other):
        # Ensure that other is a matrice
        if not isinstance(other, Matrix):
            raise TypeError("A Matrix can only be added with another matrix.")

        # Checks if the size of the 2 matrices match
        if self.x == other.x and self.y == other.y:
            
            newArr = []
            # Iterate through the row
            for x in range(self.x):
                row = []

                # Iterate through the coloumn
                for y in range(self.y):
                    # Adds all the element to its corresponding element
                    row.append(self.matrix[x][y] + other.matrix[x][y])
                
                newArr.append(row)

            return Matrix(newArr)
        else:
            raise SizeMismatchError("Matrices are not of the same size.")

    # Subtract two vector from it's corresponding element
    def __sub__(self, other):
        # Ensure that other is a matrice
        if not isinstance(other, Matrix):
            raise TypeError("A Matrix can only be subtracted with another Matrix.")
            
        # Checks if the size of the 2 matrices match
        if self.x == other.x and self.y == other.y:
			
            newArr = []
            # Iterate through the row
            for x in range(self.x):
                row = []

                # Iterate through the coloumn
                for y in range(self.y):
                    # Subtract all the element to its corresponding element
                    row.append(self.matrix[x][y] - other.matrix[x][y])
                
                newArr.append(row)

            return Matrix(newArr)
        else:
            raise SizeMismatchError("Matrices are not of the same size")

    # Multiplies matrice with a number or another matrice with it's corresponding element
    def __mul__(self, other):
        # If the other number, perform a scalar multiplication
        if isinstance(other, int) or isinstance(other, float):
            # Multiply the matrice by a scalar quantity
            newArr = []

            # Iterate through the row
            for x in range(self.x):
                row = []
                
                # Iterate through the coloumn
                for y in range(self.y):
                    # Multiply each element by n
                    row.append(self.matrix[x][y] * other)
                newArr.append(row)

            return Matrix(newArr)

        # Checks if the matrice is of the same size
        elif self.x == other.x and self.y == other.y:
            newArr = []
            # Iterate through the row
            for x in range(self.x):
                row = []
                # Iterate through the coloumn
                for y in range(self.y):
                    # Multiply all the element to its corresponding element
                    row.append(self.matrix[x][y] * other.matrix[x][y])
                newArr.append(row)

            return Matrix(newArr)
        else:
            raise TypeError("A Matrix can only be multiplied with other Matrices of the same shape or with a number.")

    # Divides two vector or  from it's corresponding element
    def __truediv__(self, other):
        # If the other number, perform a scalar divisoin
        if isinstance(other, int) or isinstance(other, float):
            # Multiply the matrice by a scalar quantity
            newArr = []

            # Iterate through the row
            for x in range(self.x):
                row = []
                
                # Iterate through the coloumn
                for y in range(self.y):
                    # Divide each element by n
                    row.append(self.matrix[x][y] / other)
                newArr.append(row)

            return Matrix(newArr)

        # Checks if the vector is of the same size
        elif self.x == other.x and self.y == other.y:
            newArr = []
            # Iterate through the row
            for x in range(self.x):
                row = []
                # Iterate through the coloumn
                for y in range(self.y):
                    # Multiply all the element to its corresponding element
                    row.append(self.matrix[x][y] / other.matrix[x][y])
                newArr.append(row)

            return Matrix(newArr)
        else:
            raise TypeError("A Matrix can only be divided with other Matrices of the same shape or with a number.")

    # Compare 
    def __eq__(self, other):
        # Check shape
        if self.x == other.x and self.y == other.y:
            # Check individual values
            for row in range(self.x):
                for col in range(self.y):
                    if self[row][col] != other[row][col]:
                        return False
            
            # Or else return false
            return True

        else:
            return False


    # Get a specific column
    def column(self, y):
        newArr = []
        # Iterate through each row
        for x in range(self.x):
            # Append the required column element
            newArr.append(self.matrix[x][y])

        return newArr

    # So that we can iterate through the vector
    def flatten(self):
        newArr = []
        # Iterate through the row
        for x in range(self.x):
            # Iterate through the coloumn
            for y in range(self.y):
                newArr.append(self.matrix[x][y])

        return newArr

    # Transpose
    def T(self):
        # Perform the matrice transpose operation
        transposed = []

        for x in zip(*self.matrix):
            transposed.append(list(x))

        return Matrix(transposed)

    # This function performs matrice multiplication
    def multiply(self, other):
        # Ensure that the other factor is also a matrice
        if not isinstance(other, Matrix):
            raise TypeError("Matrix multiplication can only be performed with other matrices.")
        
        # This column and the other row must match
        elif self.y == other.x:
            newArr = []

            # Iterate through each row in matrice A
            for row_A in range(self.x):
                row = []
                # Iterate through each column in matrice B
                for column_B in range(other.y):
                    total = 0
                    # Iterate through the column in matrice A which is also the row in the matrice B
                    for i in range(self.y):
                        total += self[row_A][i] * other[i][column_B]
                    # Append the total the current row
                    row.append(total)
                # Append row to the matrice
                newArr.append(row)

            return Matrix(newArr)    
        
        else:
            raise SizeMismatchError("A Matrix multiplcation can only be performed if the number of columns of 'A' matches the number of rows of 'B'.")
        

