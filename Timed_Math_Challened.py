import random
import time


OPERATOR = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def genrate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    operator = random.choice(OPERATOR)

    expression = f"{str(left)} {operator} {str(right)}"
    answer = eval(expression)
    return expression, answer

wrong = 0
input("Press enter to start!")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expression, answer = genrate_problem()
    while True:
        guess = input(f"Problem #{str(i+1)}: {expression} = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()

total_time = round(end_time - start_time, 3)

print("----------------------")
print(f"Nice work! You Finished in {total_time} seconds!")



