from SUBMIT.random_case_generator import random_generate
from algo_bonus import SAT2_Solver
from algo_final import MAIN
import time

# the time complexity depends on the number of literals instead of number of clauses


result = []
for num_liter in [5,10,20,30]:
    case = random_generate(num_liter, num_liter)
    a = time.time()
    MAIN(case[0], case[1], case[2])
    b = time.time()
    SAT2_Solver(case[0], case[1], case[2])
    c = time.time()
    result.append([b-a, c-b])

    print(result)
