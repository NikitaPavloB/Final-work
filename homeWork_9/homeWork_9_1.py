import csv
import json
import random
import os


# Функция для генерации CSV-файла
def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(rows):
            a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
            writer.writerow([a, b, c])


# Функция для нахождения корней квадратного уравнения
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2


# Декоратор для сохранения результатов в JSON
def save_to_json(func):
    def wrapper(file_name):
        results = []
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                a, b, c = map(int, row)
                roots = func(a, b, c)
                result_entry = {"parameters": [a, b, c], "result": roots}
                results.append(result_entry)

        with open('results.json', 'w') as jsonfile:
            json.dump(results, jsonfile, indent=4)

    return wrapper


# Применение декоратора к функции find_roots
@save_to_json
def find_roots_with_saving(a, b, c):
    return find_roots(a, b, c)


# Пример использования
generate_csv_file("input_data.csv", 101)
find_roots_with_saving("input_data.csv")

# Проверка результата
with open("results.json", 'r') as f:
    data = json.load(f)

if 100 <= len(data) <= 1000:
    print(True)
else:
    print("Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data) == 101)
