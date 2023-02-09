# Задача №1 "Ферма Дядюшки Джо"
# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:

# гусей "Серый" и "Белый"
# корову "Маньку"
# овец "Барашек" и "Кудрявый"
# кур "Ко-Ко" и "Кукареку"
# коз "Рога" и "Копыта"
# и утку "Кряква"​Со всеми животными вам необходимо как-то взаимодействовать:
# кормить
# корову и коз доить
# овец стричь
# собирать яйца у кур, утки и гусей
# различать по голосам(коровы мычат, утки крякают и т.д.)​
# Задание 1:
# Нужно реализовать классы животных и определить методы взаимодействия с животными.
# ​Для каждого животного из списка должен существовать экземпляр класса.
# Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.​

# Задание 2:
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).

# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.
# Задача №2 "Аудиоколлекция"
class Animals:
    def __init__(self, name="", weight=0):
        self.name = name
        self.weight = weight

    def feed(self, values):
        self.weight += values
        return "Покормили"


class Egg_Laying(Animals):
    def do_smth(self):
        return "несет яица"


class Chicken(Egg_Laying):
    representative = "Курица"

    def voice(self):
        return "Квак"


class Duck(Egg_Laying):
    representative = "Утка"

    def voice(self):
        return "Кря"


class Goose(Egg_Laying):
    represantative = "Гусь"

    def voice(self):
        return "Уаа"


class Shearing(Animals):
    def do_smth(self):
        return "cтрижется"


class Sheep(Shearing):
    representative = "Овца"

    def voice(self):
        return "Биии"


class Milking(Animals):
    def do_smth(self):
        return "доется"


class Cow(Milking):
    representative = "Корова"

    def voice(self):
        return "Мууу"


class Goat(Milking):
    representative = "Коза"

    def voice(self):
        return "Беее"


feed_value = 1
farm = [
    Chicken("Петушок", 5),
    Chicken("Ку-ку", 6),
    Goose("Гусар", 11),
    Goose("Гисар", 15),
    Duck("Кряк", 8),
    Sheep("Барашек", 100),
    Sheep("Кудряш", 94),
    Cow("Бурёнка", 250),
    Goat("Рогонавт", 65),
    Goat("Копатыч", 85),
]

for animal in farm:
    print(f'Его зовут {animal.name}, он весит {animal.weight} кг, говорит {animal.voice()} и {animal.do_smth()}')




