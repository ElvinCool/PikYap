import json
import sys
import random
from contextlib import contextmanager
from time import time

# Декоратор для вывода результата
class print_result:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        print(result)
        return result

# Контекстный менеджер для измерения времени
@contextmanager
def cm_timer_1():
    start_time = time()
    yield
    print(f"Time elapsed: {time() - start_time:.2f} seconds")

# Определяем путь к файлу
path = 'lab4/data_light.json'

# Загрузка данных
with open(path, encoding='utf-8') as f:
    data = json.load(f)

# Реализация функций
@print_result
def f1(arg):
    return sorted(set(job["job-name"].strip().lower() for job in arg), key=str.casefold)

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith("программист"), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    salaries = [random.randint(100000, 200000) for _ in range(len(arg))]
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(arg, salaries)]

# Основной блок
if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))