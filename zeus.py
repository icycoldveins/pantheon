import numpy as np

# give transpose


def transpose(matrix):
    return np.transpose(matrix)
# give eigenvalues for given matrix


def eigenvalues(matrix):
    return np.linalg.eigvals(matrix)


def eigenvectors(matrix):
    return np.linalg.eig(matrix)


def determinant(matrix):
    return np.linalg.det(matrix)
# find trace of the given matrix


def trace(matrix):
    return np.trace(matrix)
def inverse (matrix):
    return np.linalg.inv(matrix)
def main():
    matrix2x2 = np.array([[-4, 1], [-6, 1]])
    print(eigenvectors(matrix2x2))

main()
