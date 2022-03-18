from random_case_generator import random_generate
from SAT2_Solver import SAT2_Solver
from Kosaraju import kosaraju
import time
import numpy as np
import matplotlib.pyplot as plt

# the time complexity depends on the number of literals instead of number of clauses

upper_bound = 20
factor = 2 # number_literal = n, number_clauses = n*factor

pre_b_a = pre_c_b = 0
result = np.zeros((upper_bound,2)) #kosa, dpll
for n in range(2,upper_bound):
    case = random_generate(round(n), round(n*factor))
    a = time.time()
    kosaraju(case[0], case[1], case[2])
    b = time.time()
    SAT2_Solver(case[0], case[1], case[2])
    c = time.time()
    #smooth curve
    b_a,c_b = b-a, c-b
    if b_a == 0:
        b_a = pre_b_a
    if c-b:
        c_b = pre_c_b
    
    result[n] =(b_a,c_b)
    pre_b_a = b-a
    pre_c_b = c-b
    
print(result)

xdata = range(2,upper_bound)
y1 = result[2:,0]
y2 = result[2:,1]
plt.figure(figsize=(5, 2.7))
plt.plot(xdata, y1, label='Kosaraju')  
plt.plot(xdata, y2, label='SAT2_Solver')
plt.xlabel('Number of literals')
plt.ylabel('Running Time')
plt.title("Number of literals = Number of clauses*2")
plt.legend()