import random
def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min >= max:
        return []

    if quantity < 1 or quantity > (max - min + 1):
        return []

    numbers = set()

    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return list(numbers)


result = get_numbers_ticket(1, 1000, 5)
print(result)