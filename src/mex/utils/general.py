def convert_min(table):
    """
    If the problem to solve is maximization it is analogue to solve the problem -minimization. So this function multiply by -1 the objective function for maximization problems.
    """
    
    table[-1,:-2] = [-1*i for i in table[-1,:-2]]
    table[-1,-1] = -1*table[-1,-1]    
    
    return table

def gen_var(table):
    """
    Generates the required number of variables. They are defined by the problem.
    """
    
    lc = len(table[0,:])
    lr = len(table[:,0])
    
    var = lc - lr -1
    v = []
    
    for i in range(var):
        v.append('x'+str(i+1))
    
    return v
