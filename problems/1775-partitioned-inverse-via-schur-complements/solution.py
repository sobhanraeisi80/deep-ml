import numpy as np
import math
def partition_block_matrix(M, k):
    E = M[:k,:k]
    H = M[k:, k:]
    G = M[k:,:k]
    F = M[:k, k:]
    return (E, F, G, H)

def partitioned_inverse(M, k):
    E, F, G, H = partition_block_matrix(M, k)
    H_inv = np.linalg.inv(H)
    M_H = E - F @ H_inv @ G
    M_H_inv = np.linalg.inv(M_H)

    return np.block([[M_H_inv, -1 * M_H_inv @ F @ H_inv],
                     [-1 * H_inv @ G @ M_H_inv, H_inv + H_inv @ G @ M_H_inv @ F @ H_inv]])

def block_slogdet(M, k):
    E, F, G, H = partition_block_matrix(M, k)
    H_inv = np.linalg.inv(H)
    M_H = E - F @ H_inv @ G
    determinant = np.linalg.det(H) * np.linalg.det(M_H)
    return np.array([determinant // math.fabs(determinant), round(math.log(math.fabs(determinant), math.e), 4)])
def bordered_inverse(A_inv, b, c):
    A = np.linalg.inv(A_inv)
    b_t = b.reshape(-1, 1)
    s = c - b_t.T @ A_inv @ b_t
    if math.fabs(s.item()) < 1e-12:
        raise ValueError
    return partitioned_inverse(np.block([[A, b_t],
                                  [b_t.T, c]]), A.shape[0])