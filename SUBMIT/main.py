# -*- coding: utf-8 -*-
from base_classes import *
from check_validation import check_validation
from construct_bool_dict import construct_bool_dict
from Kosaraju import kosaraju
from parse import parse
from SAT2_Solver import SAT2_Solver
from random_case_generator import random_generate
import random
import time

test_cases = []
for i in range(10):
    random.seed(int(time.time()))
    test_cases.append(random_generate(i*2,i*3)) 
print("test_cases: ",test_cases)

for case in test_cases:
    print("testcase: ",case)
    res_kosa, unsat, sol_kosa = kosaraju(case[0],case[1],case[2])
    res_ori, sol_ori = SAT2_Solver(case[0],case[1],case[2])
     
    if res_kosa == res_ori:
        print("same result: ", res_kosa)
        if res_kosa == 'UNSATISFIABLE':
            print('UNSATISFIABLE')
        else:
            sol_kosa = construct_bool_dict(sol_kosa)
            sol_ori = construct_bool_dict(sol_ori)
            
            valid_kosa = check_validation(case[2], sol_kosa)[0]
            valid_ori = check_validation(case[2], sol_ori)[0]
            
            if valid_kosa == valid_ori == True:
                print("solution valid")
            else:
                print(valid_kosa, valid_ori)
                print("solution invalid")
    else:
        print("different result")

