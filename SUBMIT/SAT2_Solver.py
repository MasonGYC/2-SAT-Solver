# -*- coding: utf-8 -*-
import numpy as np

def SAT2_Solver(num_literals, num_clauses, cnf):
    """
    :param num_literals: number of literals
    :param num_clauses: number of clauses
    :param cnf: a cnf expression, in terms of a nested list
    :return: bool, result list(if satisfied) / None(if unsatisfied)
    """
    cnf = np.array(cnf)

    # construct a literal-bool mapping dict
    boolean_value = {}
    for literal in np.unique(cnf):
        if literal > 0:
            boolean_value[literal] = False
            boolean_value[-literal] = True
        else:
            boolean_value[literal] = True
            boolean_value[-literal] = False

    maximum_step = 100*num_literals**2  # set maximum steps
    step = 0
    satisfiable = False

    while step < maximum_step:
        step += 1
        validation, unsatisfied_clauses = check_validation(cnf, boolean_value)
        if validation:
            satisfiable = True
            break
        # else cnf is not valid

        # randomly pick one literal from unsatisfied clauses
        target_clause = random.choice(unsatisfied_clauses)
        target_literal = random.choice(target_clause)
        boolean_value[target_literal] = not boolean_value[target_literal]
        boolean_value[-target_literal] = not boolean_value[target_literal]

    if satisfiable:
        # convert the result to proper cnf type
        result = [None]*num_literals
        for i in boolean_value.keys():
            if i < 0:
                pass
            else:
                # True 1; False 0
                result[i-1] = 1 if boolean_value[i] else 0
        return "SATISFIABLE", result
    return "UNSATISFIABLE", None
