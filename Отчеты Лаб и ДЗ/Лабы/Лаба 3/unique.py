class Unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items)  # Преобразуем входные данные в итератор
        self.seen = set()  # Множество для отслеживания уникальных элементов
        self.ignore_case = kwargs.get('ignore_case', False)  # Получаем параметр ignore_case

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            current = next(self.items)  # Получаем следующий элемент из итератора
            
            # Преобразуем в нижний регистр, если ignore_case=True и элемент — строка
            check_value = current.lower() if self.ignore_case and isinstance(current, str) else current
            
            # Проверяем, был ли элемент уже обработан
            if check_value not in self.seen:
                self.seen.add(check_value)  # Добавляем в seen, чтобы не повторять
                return current  # Возвращаем исходное значение без изменения регистра

if __name__ == "__main__":
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(list(Unique(data)))  

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data)))  
    print(list(Unique(data, ignore_case=True))) 
