class Date:
    """
    Клас для представлення дати.

    Атрибути:
    - day (int): День.
    - month (int): Місяць.
    - year (int): Рік.
    """
    def __init__(self, day, month, year):
        """
        Ініціалізує об'єкт Date.

        Аргументи:
        - day (int): День, який має бути у межах 1-31.
        - month (int): Місяць, який має бути у межах 1-12.
        - year (int): Рік.
        
        Піднімає:
        - ValueError: Якщо день або місяць знаходяться поза межами допустимих значень.
        """
        if month < 1 or month > 12 or day < 1 or day > 31:
            raise ValueError("Некоректна дата")
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """
        Повертає рядкове представлення дати.

        Повертає:
        - str: Дата у форматі "DD/MM/YYYY".
        """
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def __eq__(self, other):
        """
        Перевантажує оператор == для порівняння дат.

        Аргументи:
        - other (Date): Інший об'єкт Date для порівняння.

        Повертає:
        - bool: True, якщо дати рівні, False - якщо ні.
        """
        return (self.day, self.month, self.year) == (other.day, other.month, other.year)

    def __lt__(self, other):
        """
        Перевантажує оператор < для порівняння дат.

        Аргументи:
        - other (Date): Інший об'єкт Date для порівняння.

        Повертає:
        - bool: True, якщо поточна дата менша, False - якщо ні.
        """
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def is_leap_year(self):
        """
        Перевіряє, чи є рік високосним.

        Повертає:
        - bool: True, якщо рік високосний, False - якщо ні.
        """
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

if name == "__main__":
    date1 = Date(12, 4, 2025)
    print(date1)

    date2 = Date(29, 2, 2024)
    print(date2.is_leap_year())

    print(date1 == date2)
    print(date1 < date2)