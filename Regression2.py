import random
import copy

def test_function(function):
    all_points = 0
    amnt = len(right_answers)
    a = function[0]
    b = function[1]
    c = function[2]

    for i in right_answers:
        x = i[0]
        y = a*(x*x) + b*x + c

        difference = i[1] - y
        if difference < 0:
            difference *= -1
        
        all_points += difference
    final_points = all_points/amnt

    return final_points

right_answers = [
    [1, 19],
    [2, 36],
    [5, 135],
    [0, 10],
    [-1, 9]
]

x = 0
y = 0
function = [1,1,0]
functions = [[function, test_function(function)]]
# f(x) = ax*x + bx + c
# f(x) = 2x*x + 1x + 0

for i in range(250000):
    
    if i%1000 == 0:
        print(i)
    for x in range(10):
        
        
        new_function = copy.deepcopy(function)
        #print('antes:',new_function)
        add_a_amount = random.randint(1,500)/10
        add_a_amount *= 1 if x <= 5 else -1
        while new_function[0] + add_a_amount == 0:
            add_a_amount = random.randint(1,500)/10
            add_a_amount *= 1 if x <= 5 else -1
        new_function[0] += add_a_amount
        functions.append([new_function, test_function(new_function)])
        #input(f'dps:{new_function}')
        
    for x in range(10):
        
        
        new_function = copy.deepcopy(function)
        #print('antes:',new_function)
        add_b_amount = random.randint(1,500)/10
        add_b_amount *= 1 if x <= 5 else -1
        new_function[1] += add_b_amount
        functions.append([new_function, test_function(new_function)])
        #input(f'dps:{new_function}')

    for x in range(10):
        
        new_function = copy.deepcopy(function)
        #print('antes:',new_function)
        add_c_amount = random.randint(1,500)/10
        add_c_amount *= 1 if x <= 5 else -1
        new_function[2] += add_c_amount
        functions.append([new_function, test_function(new_function)])
        #input(f'dps:{new_function}')

    for i in functions:
        #print(test_function(function))
        #print(i[1])
        #print(i[0])
        #print()
        #print()
        #input()
        if i[1] < test_function(function):
            function = i[0]
        
    
    functions = []
print(f'Ideal function: f(x) = 4x*x + 5x + 10')
# print(function , test_function(function))   
print(f"the closest one func: f(x) = {function[0]}x*x + {function[1]}x + {function[2]}")
    

        






