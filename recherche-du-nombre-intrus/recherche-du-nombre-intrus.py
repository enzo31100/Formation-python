import random

def input_list_numbers(size, intrus):
    integer_number = random.randint(0, 425)
    numbers = [integer_number] * size
    intrus_index = random.randint(0,size -1)
    numbers[intrus_index] = intrus
    return numbers

def detect_numbers_intrus(numbers):
    "On utilise un dictionnaire pour compter les occurence"
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    for number,count in counts.items():
        if count == 1:
            return number
    return None
def filter_positive_numbers(numbers):
    return [number for number in numbers if number > 0]

def difference_list(list1, list2):
    return list(set(list1) - set(list2))


def start_game():
    size = 10
    intrus = random.randint(1,100)
    numbers = input_list_numbers(size,intrus)
    print("Voici la liste des nombres : ")
    print(numbers)
    intruder = detect_numbers_intrus(numbers)
    print(f"L'intrus detecté est {intruder}")
    positive = filter_positive_numbers(numbers)
    print("Les nombres positifs dans la liste sont : ")
    print(positive)
    difference = difference_list(numbers, [intruder])
    print("La liste après avoir enlever l'intrus : ")
    print(difference)

if __name__ == '__main__':
    start_game()
