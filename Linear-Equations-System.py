import numpy as np

variables = {}
solutions = []
numbers = ["0","1","2","3","4","5","6","7","8","9"]
sign = ["+","-"]

amount = int(input())
for i in range(amount):
    coef , solu = input().split("=")
    solu = int(solu)
    solutions.append(solu)
    for i in coef:
        if i in sign:
            num = i
        elif i in numbers:
            num += i
        else:
            if i in variables:
                variables[i].append(int(num))  
            else:
                variables[i] = [int(num)]

variables = dict(sorted(variables.items()))
coefficients = []
for i in variables:
    coefficients.append(variables[i])
    
coefficients = np.array(coefficients).reshape(amount, amount).transpose()       
solutions = np.array(solutions)

result = np.linalg.solve(coefficients, solutions).flatten()

result2 = ''
count = 0
for i in variables:
    result2 += i+"="+str(format(result[count], ".2f"))
    if count != amount-1:
        result2 += " | "
    count += 1

print(result2)


            
        
            
    
    