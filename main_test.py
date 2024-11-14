import unittest
from refact_main import Computer, Browser, ComputerBrowser, one_to_many, many_to_many, get_browsers_with_computers, get_browsers_with_avg_processing, get_computers_with_browsers_starting_with_A

class TestComputerBrowserFunctions(unittest.TestCase):
    def setUp(self):
        # Инициализация тестовых данных
        self.computers = [
            Computer(1, 'Андреев', 3.2, 1),
            Computer(2, 'Петров', 4.1, 2),
            Computer(3, 'Антонов', 2.9, 1),
            Computer(4, 'Иванов', 4.0, 3),
            Computer(5, 'Смирнов', 3.0, 1),
        ]

        self.browsers = [
            Browser(1, 'Интернет-браузер Chrome'),
            Browser(2, 'Браузер безопасности Firefox'),
            Browser(3, 'Мобильный браузер Safari'),
        ]

        self.computer_browsers = [
            ComputerBrowser(1, 1),
            ComputerBrowser(2, 2),
            ComputerBrowser(3, 1),
            ComputerBrowser(4, 3),
            ComputerBrowser(5, 1),
        ]

    def test_get_browsers_with_computers(self):
        one_to_many_result = one_to_many(self.computers, self.browsers)
        expected = {
            'Интернет-браузер Chrome': ['Андреев', 'Антонов', 'Смирнов'],
            'Браузер безопасности Firefox': ['Петров'],
            'Мобильный браузер Safari': ['Иванов']
        }
        self.assertEqual(get_browsers_with_computers(one_to_many_result), expected)

    def test_get_browsers_with_avg_processing(self):
        one_to_many_result = one_to_many(self.computers, self.browsers)
        expected = [
            ('Интернет-браузер Chrome', 3.03),
            ('Мобильный браузер Safari', 4.0),
            ('Браузер безопасности Firefox', 4.1)
        ]
        self.assertEqual(get_browsers_with_avg_processing(one_to_many_result), expected)

    def test_get_computers_with_browsers_starting_with_A(self):
        many_to_many_result = many_to_many(self.computers, self.browsers, self.computer_browsers)
        expected = {
            'Андреев': ['Интернет-браузер Chrome'],
            'Антонов': ['Интернет-браузер Chrome']
        }
        self.assertEqual(get_computers_with_browsers_starting_with_A(many_to_many_result), expected)

if __name__ == '__main__':
    unittest.main()
