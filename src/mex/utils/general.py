def convert_min(table):
    """
    If the problem to solve is maximization it is analogue to solve the problem -minimization.
    So this function multiply by -1 the objective function for maximization problems.
    """
    
    table[-1, :-2] = [-1*i for i in table[-1, :-2]]
    table[-1, -1] = -1*table[-1, -1]
    
    return table


def gen_var(table):
    """
    Generates the required number of variables. They are defined by the problem.
    """
    
    lc = len(table[0, :])
    lr = len(table[:, 0])
    
    var = lc - lr -1
    v = []
    
    for i in range(var):
        v.append('x'+str(i+1))
    
    return v


def convert(eq):
    """
    Converts equation into a list containing the coefficients of the equation.
    """
    
    eq = eq.split(',')
    
    if 'G' in eq:
        g = eq.index('G')
        del eq[g]
        eq = [float(i)*-1 for i in eq]
        return eq
    
    if 'L' in eq:
        l = eq.index('L')
        del eq[l]
        eq = [float(i) for i in eq]
        return eq
    
    if 'E' in eq:
        l = eq.index('E')
        del eq[l]
        eq = [float(i) for i in eq]
        return eq
