def hill_climbing():
    current = 1

    while True:
        next_value = current + 1

        if next_value > 5:
            break

        current = next_value
        print("Current value:", current)

    print("Best value:", current)

hill_climbing()
