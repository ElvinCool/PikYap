data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    # С использованием lambda-функции
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)

    # Без использования lambda-функции
    def abs_key(x):
        return abs(x)

    result = sorted(data, key=abs_key, reverse=True)
    print(result)
