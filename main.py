while True:
    age = input("How old are you? (or 'quit') ")
    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    print(f"Your ticket costs ${price}.")