import random
import copy

def test_function(function):
    all_points = 0
    amnt = len(right_answers)
    a = function[0]
    b = function[1]

    for i in right_answers:
        x = i[0]
        y = a * x + b

        difference = i[1] - y
        if difference < 0:
            difference *= -1
        
        all_points += difference
    final_points = all_points/amnt

    return final_points

right_answers = [
    [1, 10],
    [2, 18],
    [5, 42],
    [0, 2],
    [-1, -6]
]

x = 0
y = 0
function = [1,0]
functions = [[function, test_function(function)]]
# f(x) = ax + b
# f(x) = x + 1

for i in range(5000):
    for x in range(10):
        new_function = copy.deepcopy(function)
        #print('new_function before', new_function)
        #input()
        add_a_amount = random.randint(1,10)/10
        add_a_amount *= 1 if x <= 5 else -1
        while new_function[0] + add_a_amount == 0:
            add_a_amount = random.randint(1,10)/10
            add_a_amount *= 1 if x <= 5 else -1
        new_function[0] += add_a_amount


        #print(add_a_amount, add_b_amount)
        #print('new_function after', new_function)
        #input()

        #print('Functions before', functions)
        #input()
        functions.append([new_function, test_function(new_function)])
        #print('Functions after', functions)
        #input()
    for x in range(10):
        new_function = copy.deepcopy(function)
        add_b_amount = random.randint(1,10)/10
        add_b_amount *= 1 if x <= 5 else -1
        new_function[1] += add_b_amount
        functions.append([new_function, test_function(new_function)])

    for i in functions:
        
        if i[1] < test_function(function):
            function = i[0]
        
    
    functions = []

print(function , test_function(function))        
print("ideal function: f(x) = 8x + 2")
print(f"the closest one func: f(x) = {function[0]}x + {function[1]}")
    

        






