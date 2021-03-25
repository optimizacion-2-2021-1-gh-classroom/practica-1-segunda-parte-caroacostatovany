import numpy as np

from src.mex.utils.general import gen_var, convert
from src.mex.simplex.simplex import next_round_r, loc_piv_r, pivot, next_round, loc_piv, convert_min


def add_cons(table):
    """
    Check if 1 extra constraints can be added to the matrix, this means that there are at least two rows of all 0 elements. If this condition is not satisfied, our program will not allow the user to add additional constraints.
    """
    
    lr = len(table[:,0])
    empty = []
    
    for i in range(lr):
        total = 0
        for j in table[i,:]:
            total += j**2
        if total == 0:
            empty.append(total)
    
    if len(empty)>1:
        return True
    else:
        return False
    
    
def constrain(table, eq):
    """
    Add constraints to the problem.
    """
    if add_cons(table):
        lc = len(table[0,:])
        lr = len(table[:,0])
        var = lc - lr -1
        j = 0
        while j < lr:
            row_check = table[j,:]
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
            i +=1
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
        for j in table[i,:]:
            total += j**2
        if total == 0:
            empty.append(total)
    if len(empty)==1:
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