class		Browser:
		def
__init__(self, browser_id, name):
self.browser_id = browser_id
self.name = name

class Computer:
def __init__(self, computer_id, owner_name, processing_power, browser_id = None):
self.computer_id = computer_id
self.owner_name = owner_name
self.processing_power = processing_power
#количественный признак (например, мощность процессора)
self.browser_id = browser_id
#для связи один-ко-многим с Browser

class ComputerBrowser:
def __init__(self, computer_id, browser_id):
self.computer_id = computer_id
self.browser_id = browser_id

#Тестовые данные
browsers =[
	   Browser(1, "Инте�84нет-б�84аузе�84 Chrome"),
	   Browser(2, "Б�84аузе�84 безопасности Firefox"),
	   Browser(3, "Мобильный б�84аузе�84 Safari")
]

computers =[
	    Computer(1, "Анд�91еев", 3.2, 1),
	    Computer(2, "Пет�91ов", 4.1, 2),
	    Computer(3, "Антонов", 2.9, 1),
	    Computer(4, "Иванов", 4.0, 3),
	    Computer(5, "Сми�91нов", 3.0, 1)
]

computer_browsers =[
		    ComputerBrowser(1, 1),
		    ComputerBrowser(2, 2),
		    ComputerBrowser(3, 1),
		    ComputerBrowser(4, 3),
		    ComputerBrowser(5, 1)
]

#Запрос 1: Список браузеров с "браузер" в названии и компьютеры, использующие их
browsers_with_keyword =[
			(browser.name,[c.owner_name for c in computers if c.browser_id == browser.browser_id])
	 for browser in browsers if "б�70аузе�70" in browser.name.lower()
]
	print("Список б�63аузе�63ов с 'б�63аузе�63' и использующие их компьюте�63ы:", browsers_with_keyword)

#Запрос 2: Список браузеров со средней мощностью компьютеров, отсортированный по средней мощности
		average_processing_by_browser =[
						(browser.name, round(
								     sum(c.processing_power for c in computers if c.browser_id == browser.browser_id) /
	len([c for c in computers if c.browser_id == browser.browser_id]), 2
								     ))
						for browser in browsers if any(c.browser_id == browser.browser_id for c in computers)
		]
average_processing_by_browser.sort(key = lambda x:x[1])
			print("Б�175аузе�175ы со с�175едней мощностью компьюте�175ов:", average_processing_by_browser)

#Запрос 3: Список компьютеров с владельцами на "А" и названия используемых браузеров
			computers_with_a =[
					   (c.owner_name,[b.name for b in browsers if b.browser_id == cb.browser_id])
			 for c in computers if c.owner_name.startswith("А")
					   for cb in computer_browsers if cb.computer_id == c.computer_id
			]
			print("Компьюте�175ы с владельцами на 'А' и их б�175аузе�175ы:", computers_with_a)
