import random
def get_numbers_ticket(min,max,quantity):
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min,max))
    return numbers
result=get_numbers_ticket(1, 1000, 5)
print(result)

  