import random
import copy

def random_generate(variable, clause):
    """
    :param variable: the number of literals
    :param clause: the number of clauses
    :return: randomly generated a 2-SAT expression
    """
    generated_case = [variable, clause]

    # initialize cnf
    cnf = [[] for i in range(0, clause)]

    var_list = list(range(1,variable+1))   # variables to be filled
    clauses_list = list(range(0,clause))    # empty clauses

    # fill in all variables for at least one time
    for i in var_list:
        targeted_clause = random.choice(clauses_list)  # selected clause to be filled

        # fill targeted clause
        sign = random.randint(1, 2)
        if sign == 1:
            cnf[targeted_clause].append(i)
        else:
            cnf[targeted_clause].append(-i)
        if len(cnf[targeted_clause]) == 2:
            clauses_list.remove(targeted_clause)

    for clause in clauses_list:
        # fill in empty space
        var_list_copy = copy.deepcopy(var_list)
        if len(cnf[clause]) == 1:
            if cnf[clause][0] > 0:
                var_list_copy.remove(cnf[clause][0])
            else:
                var_list_copy.remove(-cnf[clause][0])

        for p in range(0, 2-len(cnf[clause])):
            random_index = random.randint(0, len(var_list_copy) - 1)
            insert_literal = random.choice([var_list_copy[random_index], -var_list_copy[random_index]])
            cnf[clause].append(insert_literal)

            var_list_copy.remove(var_list_copy[random_index])
    generated_case.append(cnf)

    return generated_case


