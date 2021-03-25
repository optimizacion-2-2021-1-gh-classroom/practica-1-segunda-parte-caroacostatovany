def convert_min(table):
    """
    If the problem to solve is maximization it is analogue to solve the problem -minimization. This function multiply by -1 the objective function for maximization problems.
    """
    table[-1,:-2] = [-1*i for i in table[-1,:-2]]
    table[-1,-1] = -1*table[-1,-1]    
    return table
