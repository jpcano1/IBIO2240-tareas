def productory(a: list):
	"""
	
	:param a: 
	:return: 
	"""
	result = 1
	for i in a:
		result *= i
	return result

def factorial(x: int):
	"""

	:param x:
	:return:
	"""
	if x < 0:
		raise Exception("Not a positive number")
	if x == 1 or x == 0:
		return 1
	else:
		return x*factorial(x-1)

def palindrome(number):
	number = str(number)
	pali = True
	i = 0
	while pali and i != len(number):
		if number[i] != number[-i-1]:
			pali = False
		i += 1
	return pali


def sum_matrix(mat1, mat2):
	"""
        29 - Function that allows me to sum two matrixes of NxN
        :param mat1: the first matrix to be summated
        :param mat2: the second matrix to be summated
        :return: the resulting matrix of the sum
    """

	result_mat = []
	for i in range(len(mat1)):
		row = []
		for j in range(len(mat1[i])):
			row.append(mat1[i][j] + mat2[i][j])
		result_mat.append(row)
	return result_mat