from radom_case_generator import random_generate
from algo_bonus import SAT2_Solver
from algo_final import MAIN
import time

# the time complexity depends on the number of literals instead of number of clauses


result = []
for i in range(1, 11):
    num_liter = 10**i
    case = random_generate(num_liter, num_liter**2)
    a = time.time()
    MAIN(num_liter, num_liter**2, case)
    b = time.time()
    SAT2_Solver(num_liter, num_liter**2, case)
    c = time.time()
    result.append([b-a, c-b])

print(result)