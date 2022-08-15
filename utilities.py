import random
from main import Matrix

# Returns a random vector of size (x, y)
# Eg- randomVector(2, 2)
# returns - 
#		[w, x]
#		[y, z]
def randomVector(cx, cy):
	newArr = [[random.uniform(0,1) for col in range(cy)] for row in range(cx) ]

	return Matrix(newArr)