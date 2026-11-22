def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    if len(matrix) != 2 or (len(matrix[0]) != len(matrix[1]) != 2):
        return None
    det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    if det == 0:
        return None
    return list(map(lambda x: [e * round(1 / det, 2) for e in x], 
    [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]))