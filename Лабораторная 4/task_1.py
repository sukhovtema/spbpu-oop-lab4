class Human:
    """Базовый класс Человек."""
    def __init__(self, name: str, age: int):
        """
        Инициализация объекта Человек.

        :param name: Имя человека.
        :param age: Возраст человека.
        """
        self.name = name
        self.age = age

    def greet(self) -> str:
        """Приветствие."""
        return f'Привет, меня зовут {self.name} и мне {self.age} лет.'

    def __str__(self) -> str:
        """Строковое представление объекта."""
        return f'Человек: {self.name}, Возраст: {self.age}'

    def __repr__(self) -> str:
        """Формальное строковое представление объекта."""
        return f'Human(name={self.name!r}, age={self.age!r})'


class Man(Human):
    """Дочерний класс Мужчина."""
    def __init__(self, name: str, age: int, occupation: str):
        """
        Инициализация объекта Мужчина.

        :param name: Имя мужчины.
        :param age: Возраст мужчины.
        :param occupation: Профессия мужчины.
        """
        super().__init__(name, age)
        self.occupation = occupation

    def work(self) -> str:
        """Мужская деятельность."""
        return f'Я работаю как {self.occupation}.'

    def __str__(self) -> str:
        """Строковое представление объекта."""
        return f'Мужчина: {self.name}, Возраст: {self.age}, Занятие: {self.occupation}'

    def __repr__(self) -> str:
        """Формальное строковое представление объекта."""
        return f'Man(name={self.name!r}, age={self.age!r}, occupation={self.occupation!r})'


class Woman(Human):
    """Дочерний класс Женщина."""
    def __init__(self, name: str, age: int, role: str):
        """
        Инициализация объекта Женщина.

        :param name: Имя женщины.
        :param age: Возраст женщины.
        :param role: Роль женщины в семье (мама, бабушка, ...).
        """
        super().__init__(name, age)
        self.role = role

    def take_care_of_family(self) -> str:
        """Женская забота о семье."""
        return f'Я забочусь о своей семье как {self.role}.'

    def __str__(self) -> str:
        """Строковое представление объекта."""
        return f'Женщина: {self.name}, Возраст: {self.age}, Роль: {self.role}'

    def __repr__(self) -> str:
        """Формальное строковое представление объекта."""
        return f'Woman(name={self.name!r}, age={self.age!r}, role={self.role!r})'


if __name__ == "__main__":
    human = Human(name='Артем', age=20)
    print(human)
    print(human.greet())

    man = Man(name='Паша', age=35, occupation='Разработчик питон')
    print(man)
    print(man.greet())
    print(man.work())

    woman = Woman(name='Галя', age=66, role='Бабушка')
    print(woman)
    print(woman.greet())
    print(woman.take_care_of_family())
