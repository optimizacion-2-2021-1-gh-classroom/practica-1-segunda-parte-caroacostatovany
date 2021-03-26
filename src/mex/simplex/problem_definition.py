import numpy as np

from mex.utils.general import gen_var, convert
from mex.simplex.simplex_networks import pivots_col, pivots_row, find_pivot_col, find_pivot_row, pivot


def add_cons(table):
    """
    Check if 1 extra constraints can be added to the matrix, this means that there are at least two rows of all
    0 elements. If this condition is not satisfied, our program will not allow the user to add additional constraints.
    """

    lr = len(table[:, 0])
    empty = []

    for i in range(lr):
        total = 0
        for j in table[i, :]:
            total += j**2
        if total == 0:
            empty.append(total)

    if len(empty) > 1:
        return True
    else:
        return False


def constrain(table, eq):
    """
    Add constraints to the problem.
    """

    if 'E' in eq:
        if add_cons(table):
            lc = len(table[0, :])
            lr = len(table[:, 0])
            var = lc - lr - 1
            j = 0

            while j < lr:
                row_check = table[j,:]
                total = 0
                for i in row_check:
                    total += float(i**2)
                if total == 0:
                    row = row_check
                    break
                j += 1
                
            eq = convert(eq)
            i = 0
            
            while i<len(eq)-1:
                row[i] = eq[i]
                i += 1
            
            row[-1] = eq[-1]
            #row[var+j] = 1
        
        else:
            print('Cannot add another constraint.')
        
    else:
        if add_cons(table):
            lc = len(table[0, :])
            lr = len(table[:, 0])
            var = lc - lr -1
            j = 0
            
            while j < lr:
                row_check = table[j, :]
                total = 0
                for i in row_check:
                    total += float(i**2)
                if total == 0:
                    row = row_check
                    break
                j +=1
                
            eq = convert(eq)
            i = 0
            
            while i<len(eq)-1:
                row[i] = eq[i]
                i += 1
            
            row[-1] = eq[-1]
            row[var+j] = 1
            
        else:
            print('Cannot add another constraint.')
        

def add_obj(table):
    """
    Verify if the objective function can be added.
    """
    
    lr = len(table[:,0])
    empty = []
    
    for i in range(lr):
        total = 0
        for j in table[i, :]:
            total += j**2
        if total == 0:
            empty.append(total)
    
    if len(empty) == 1:
        return True
    else:
        return False


def obj(table,eq):
    """
    Add the objective function to the tableau.
    """
    
    if add_obj(table):
        eq = [float(i) for i in eq.split(',')]
        lr = len(table[:,0])
        row = table[lr-1,:]
        i = 0
        while i<len(eq)-1:
            row[i] = eq[i]*-1
            i +=1
        row[-2] = 1
        row[-1] = eq[-1]
    else:
        print('You must finish adding constraints before the objective function can be added.')
        

def maxz(table):
    """
    Create maximization function. Determine if 1 extra pivot is required, locate the pivot element,
    pivot about it and continue the process util all negative elements have
    been removed from the last column and row.
    """
    
    while pivots_col(table):
        table = pivot(find_pivot_col(table)[0], find_pivot_col(table)[1], table)
    while pivots_row(table):
        table = pivot(find_pivot_row(table)[0], find_pivot_row(table)[1], table)
    
    lc = len(table[0, :])
    lr = len(table[:, 0])
    var = lc - lr - 1
    i = 0
    val = {}
    
    for i in range(var):
        col = table[:, i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[gen_var(table)[i]] = table[loc, -1]
        else:
            val[gen_var(table)[i]] = 0
    val['max'] = table[-1, -1]
    
    return val


def convert_min(table):
    """
    If the problem to solve is maximization it is analogue to solve the problem -minimization.
    So this function multiply by -1 the objective function for maximization problems.
    """
    
    table[-1, :-2] = [-1*i for i in table[-1, :-2]]
    table[-1, -1] = -1*table[-1, -1]
    
    return table


def minz(table):
    """
    Create minimization function. Determine if 1 extra pivot is required, locate the pivot element,
    pivot about it and continue the process util all negative elements have
    been removed from the last column and row.
    """

    table = convert_min(table)
    while pivots_col(table):
        table = pivot(find_pivot_col(table)[0], find_pivot_col(table)[1], table)
    while pivots_row(table):
        table = pivot(find_pivot_row(table)[0], find_pivot_row(table)[1], table)
    
    lc = len(table[0, :])
    lr = len(table[:, 0])
    var = lc - lr - 1
    i = 0
    val = {}
    
    for i in range(var):
        col = table[:, i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[gen_var(table)[i]] = table[loc, -1]
        else:
            val[gen_var(table)[i]] = 0
            val['min'] = table[-1, -1]*-1
    return val
