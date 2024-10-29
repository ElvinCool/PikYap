# используется для сортировки
from operator import itemgetter

class Computer:
    def __init__(self, computer_id, owner_name, processing_power, browser_id):
        self.computer_id = computer_id
        self.owner_name = owner_name
        self.processing_power = processing_power
        self.browser_id = browser_id

class Browser:
    def __init__(self, browser_id, name):
        self.browser_id = browser_id
        self.name = name

class ComputerBrowser:
    def __init__(self, computer_id, browser_id):
        self.computer_id = computer_id
        self.browser_id = browser_id

# Список браузеров
browsers = [
    Browser(1, 'Интернет-браузер Chrome'),
    Browser(2, 'Браузер безопасности Firefox'),
    Browser(3, 'Мобильный браузер Safari'),
]

# Список компьютеров
computers = [
    Computer(1, 'Андреев', 3.2, 1),
    Computer(2, 'Петров', 4.1, 2),
    Computer(3, 'Антонов', 2.9, 1),
    Computer(4, 'Иванов', 4.0, 3),
    Computer(5, 'Смирнов', 3.0, 1),
]

# Связи компьютеров и браузеров для связи многие-ко-многим
computer_browsers = [
    ComputerBrowser(1, 1),
    ComputerBrowser(2, 2),
    ComputerBrowser(3, 1),
    ComputerBrowser(4, 3),
    ComputerBrowser(5, 1),
]

def main():
    # Соединение данных один-ко-многим: браузер и компьютеры, использующие его
    one_to_many = [
        (c.owner_name, c.processing_power, b.name)
        for b in browsers
        for c in computers
        if c.browser_id == b.browser_id
    ]
    
    # Соединение данных многие-ко-многим: компьютер и браузеры, используемые компьютером
    many_to_many_temp = [
        (b.name, cb.browser_id, cb.computer_id)
        for b in browsers
        for cb in computer_browsers
        if b.browser_id == cb.browser_id
    ]
    
    # Завершаем связь многие-ко-многим
    many_to_many = [
        (c.owner_name, c.processing_power, browser_name)
        for browser_name, browser_id, computer_id in many_to_many_temp
        for c in computers if c.computer_id == computer_id
    ]

    # Задание 1: Список браузеров с "браузер" в названии и компьютеры, использующие их
    print('Задание E1: Список браузеров с "браузер" в названии и компьютеры')
    for browser in browsers:
        if "браузер" in browser.name.lower():
            print(f"Браузер: {browser.name}")
            associated_computers = [c.owner_name for c in computers if c.browser_id == browser.browser_id]
            print("Компьютеры:")
            for computer in associated_computers:
                print(f"  - {computer}")
            print()  # пустая строка для разделения

    # Задание 2: Список браузеров со средней мощностью компьютеров, отсортированный по средней мощности
    print('Задание E2: Браузеры со средней мощностью компьютеров')
    average_processing_by_browser = [
        (browser.name, round(
            sum(c.processing_power for c in computers if c.browser_id == browser.browser_id) /
            len([c for c in computers if c.browser_id == browser.browser_id]), 2
        ))
        for browser in browsers if any(c.browser_id == browser.browser_id for c in computers)
    ]
    average_processing_by_browser.sort(key=lambda x: x[1])

    for browser, avg_power in average_processing_by_browser:
        print(f"Браузер: {browser}, Средняя мощность: {avg_power}")
    print()

    # Задание 3: Список компьютеров с владельцами на "А" и названия их браузеров
    print('Задание E3: Компьютеры с владельцами на "А" и их браузеры')
    for c in computers:
        if c.owner_name.startswith("А"):
            used_browsers = [b.name for cb in computer_browsers for b in browsers if cb.computer_id == c.computer_id and cb.browser_id == b.browser_id]
            print(f"Владелец: {c.owner_name}")
            print("Браузеры:")
            for browser in used_browsers:
                print(f"  - {browser}")
            print()  # пустая строка для разделения

if __name__ == '__main__':
    main()
