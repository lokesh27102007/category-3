states = [1, 2, 3]
k = 2

for i in range(3):
    successors = []

    for state in states:
        successors.append(state + 1)
        successors.append(state + 2)

    states = sorted(successors, reverse=True)[:k]
    print("Best states:", states)

print("Final best state:", states[0])
