import numpy as np
import random

def construct_bool_dict(input_list):
    if input_list is None:
        return None
    result = {}
    for i in range(1, len(input_list)+1):
        result[i] = True if input_list[i-1]==1 else False
        result[-i] = not result[i]
    return result

def check_validation(cnf_np, bool_mapping):
    """
    check if input cnf_np's output is True
    :param cnf_np: a 2D np-array
    :param bool_mapping: (bool, unsatisfied(2D np-array))
    :return: validation(bool), unsatisfied clauses(numpy)
    """
    result = True
    unsatisfied_clauses = np.array([[0, 0]])
    for clause in cnf_np:
        if bool_mapping[clause[0]] or bool_mapping[clause[1]]:
            continue
        else:
            result = False
            unsatisfied_clauses = np.append(unsatisfied_clauses, [clause], axis=0)
    unsatisfied_clauses = np.delete(unsatisfied_clauses, 0, axis=0)

    return result, unsatisfied_clauses

def SAT2_Solver(num_literals, num_clauses, cnf):
    """
    :param num_literals: number of literals
    :param num_clauses: number of clauses
    :param cnf: a cnf expression, in terms of a nested list
    :return: bool, result list(if satisfied) / None(if unsatisfied)
    """
    #check special case
    if num_clauses == 0:
        return 'SATISFIABLE',None
    if [] in cnf:
        return 'UNSATISFIABLE',None

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

print(SAT2_Solver(0, 0, []))