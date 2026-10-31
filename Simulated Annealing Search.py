import random
import math

current = 10
temperature = 100

while temperature > 1:
    next_value = current + random.choice([-1, 1])

    if next_value > current:
        current = next_value
    else:
        probability = math.exp((next_value - current) / temperature)
        if random.random() < probability:
            current = next_value

    temperature *= 0.8

print("Final solution:", current)
