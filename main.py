def task1():
    # Ввод строки
    input_string = input("Введите строку: ")

    # Нахождение первого индекса начала фрагмента «ра»
    index = input_string.find("ра")

    # Вывод результата
    print(index)
    
    # 2
    
    # Ввод списка чисел
    input_numbers = input("Введите список целых чисел через пробел: ")
    numbers = []
    for num in input_numbers.split():
        numbers.append(int(num))

    # Вычисление суммы чисел
    total_sum = 0
    for number in numbers:
        total_sum += number

    # Вывод результата
    print(total_sum)



def task2(): 
    # Ввод строки
    input_string = input("Введите строку с арифметическим действием: ")

    # Удаление пробелов и выполнение операции сложения
    result = eval(input_string.replace(" ", ""))

    # Вывод результата
    print(result) 
    
    # 2
    
    # Ввод списка вещественных чисел
    input_floats = input("Введите список вещественных чисел через пробел: ")
    float_numbers = []
    for num in input_floats.split():
        float_numbers.append(float(num))

    # Нахождение минимального числа
    min_number = float_numbers[0]
    for number in float_numbers:
        if number < min_number:
            min_number = number

    # Вывод результата
    print(min_number)


def task3(): 
    # Ввод слова
    word = input("Введите слово: ")

    # Проверка на палиндром
    is_palindrome = word.lower() == word[::-1].lower()

    # Вывод результата
    print(is_palindrome)

    # 2
    
    # Ввод списка оценок
    input_grades = input("Введите список оценок через пробел: ")
    grades = []
    for grade in input_grades.split():
        grades.append(int(grade))

    # Подсчет количества двоек
    count_of_twos = grades.count(2)

    # Вывод результата
    print(count_of_twos)

            

def task4(): 
    import re

    # Ввод пароля
    password = input("Введите пароль: ")

    # Проверка пароля на корректность
    is_valid_password = (len(password) >= 8 and 
                        bool(re.search(r"[$#!?\-_]", password)) and 
                        bool(re.search(r"[A-D]", password)))

    # Вывод результата
    print(is_valid_password)
    
    # 2
    
    # Ввод слов
    input_words = input("Введите слова через пробел: ")
    words = input_words.split()

    # Проверка на повторение последнего слова
    is_last_word_repeated = words.count(words[-1]) > 1

    # Вывод результата
    print(is_last_word_repeated)


def task5(): 
    # Ввод фрагмента URL
    url_fragment = input("Введите фрагмент URL: ")

    # Замена всех двух подряд идущих дефисов на один
    modified_url_fragment = url_fragment.replace("--", "-")

    # Подсчет числа замен
    number_of_replacements = url_fragment.count("--")

    # Вывод результата
    print(modified_url_fragment, number_of_replacements)

    # 2
    
    # Ввод информации о студенте
    student_info = input("Введите информацию о студенте: ").split()

    # Преобразование информации в нужный формат
    name = student_info[0]
    age = int(student_info[1])
    group = student_info[2]

    grades = []
    for grade in student_info[3:]:
        grades.append(int(grade))

    # Формирование списка
    student_list = [name, age, group, grades]

    # Вывод результата
    print(student_list)

def task6():
     # Ввод строки
    input_string = input("Введите строку из нескольких слов: ")

    # Преобразование строки в список слов
    words = input_string.split()

    # Проверка на совпадение первого и последнего слова
    result = words[0] != words[-1]

    # Вывод результата
    print(result)

    # 2
    
    # Ввод списка предметов
    input_items = input("Введите список предметов: ")

    # Преобразование введенных данных в двумерный список
    items = input_items.split()
    result = []

    for item in items:
        name, weight = item.split('=')
        result.append([name, int(weight)])

    # Вывод результата
    print(result)

def task7():
    asd = 0
    
    
def task8():
    import math

    # Ввод катетов прямоугольного треугольника
    a = int(input("Введите катет a: "))
    b = int(input("Введите катет b: "))

    # Вычисление гипотенузы
    c = math.sqrt(a**2 + b**2)

    # Вычисление периметра
    perimeter = a + b + c

    # Вывод результата
    print(f"Периметр прямоугольного треугольника со сторонами {a}, {b}, {c:.1f}, равен: {perimeter:.1f}")
    # 2
    
    # Ввод списка городов
    input_cities = input("Введите список городов через пробел: ")

    # Преобразование строки в список городов
    cities = input_cities.split()

    # Вывод городов через один
    filtered_cities = cities[::2]

    # Вывод результата
    print(" ".join(filtered_cities))

    # Вывод общего числа введенных городов
    print(len(cities))



def task9():
    # # Ввод информации
    # fio = input("Введите ФИО студента: ")
    # age = input("Введите возраст: ")
    # weight = input("Введите вес: ")
    # group = input("Введите название группы: ")

    # # Объединение всех данных в одну строку
    # result = fio + " " + age + " " + weight + " " + group

    # # Вывод результата
    # print(result)

    # 2
    
    input_countries = input('Введите названия стран через пробел: ')
    
    countries = input_countries.split()
    
    countries[0], countries[-1] = countries[-1], countries[0]
    
    print(countries)
    
    russia = 'Россия' in countries
    
    print(russia)


def task10():
    # Ввод строки
    input_string = input("Введите строку: ")

    # Определение индекса вхождения фрагмента «до» с конца строки
    index = input_string.rfind("до")

    # Вывод результата
    print(index)

    # 2
    
    # Ввод строки из вещественных чисел
    input_numbers = input("Введите строку из вещественных чисел через пробел: ")

    # Преобразование строки в список вещественных чисел
    numbers = []
    for num in input_numbers.split():
        numbers.append(float(num))

    # Определение середины списка
    mid_index = len(numbers) // 2

    # Вычисление суммы первой половины списка
    sum_first_half = sum(numbers[:mid_index])

    # Вычисление суммы второй половины списка
    sum_second_half = sum(numbers[mid_index:])

    # Вывод результатов с точностью до сотых
    print(f"{sum_first_half:.2f}")
    print(f"{sum_second_half:.2f}")


def task11():
    # Ввод трех целых чисел
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    c = int(input("Введите число c: "))

    # Нахождение минимального значения с использованием условного оператора if
    if a <= b and a <= c:
        min_value = a
    elif b <= a and b <= c:
        min_value = b
    else:
        min_value = c

    # Вывод минимального значения
    print(min_value)
    
    # 2
    
    # Ввод двух целых чисел
    m = int(input("Введите число m: "))
    n = int(input("Введите число n: "))

    # Проверка делимости и вычисление результата с использованием тернарного условного оператора
    result = m // n if n != 0 and m % n == 0 else m * n

    # Вывод результата
    print(result)

def task12():
    # Ввод натурального четырехзначного числа
    number = int(input("Введите натуральное четырехзначное число: "))

    # Проверка на четырехзначность числа
    if 1000 <= number <= 9999:
        # Вычисление суммы или произведения цифр в зависимости от кратности числа трем
        digits = [int(digit) for digit in str(number)]
        if number % 3 == 0:
            result = sum(digits)
        else:
            result = 1
            for digit in digits:
                result *= digit
            
        # Вывод результата
        print(f"Результат: {result}")
    else:
        print("Число не является четырехзначным")

    # 2
    
    # Представление меню в виде многострочной строки
    menu = """
    Меню:
    1. Кафедра ТК
    2. Факультет ФИСТ
    3. Кафедра Радиотехника
    4. Выход из программы
    """

    # Вывод меню на экран
    print(menu)

    # Ввод пункта меню от пользователя
    choice = int(input("Введите номер пункта меню: "))

    # Определение выбранного пункта меню с помощью условного оператора if-elif-else
    if choice == 1:
        print("Выбран Кафедра ТК пункт меню")
    elif choice == 2:
        print("Выбран Факультет ФИСТ пункт меню")
    elif choice == 3:
        print("Выбран Кафедра Радиотехника пункт меню")
    elif choice == 4:
        print("Выбран Выход из программы пункт меню")
    else:
        print("Такой пункт не найден")

def task13():
    # Ввод натурального числа
    number = int(input("Введите натуральное число: "))

    # Определение трехзначности числа с использованием строковой длины числа
    message = "Трехзначное число" if 100 <= number <= 999 else "Не трехзначное число"

    # Вывод результата
    print(message)

    # 2
    
    # Ввод двух натуральных чисел
    a = int(input("Введите время в секундах: "))
    b = int(input("Введите время в минутах: "))

    # Определение наибольшего времени с использованием тернарного условного оператора
    max_time = a if a > b * 60 else b * 60

    # Вывод результата
    print(f"Наибольшее время: {max_time} секунд")


def task14():
    # Ввод вещественных положительных чисел
    a = float(input("Введите сторону a прямоугольника: "))
    b = float(input("Введите сторону b прямоугольника: "))
    c = float(input("Введите сторону c прямоугольника: "))
    d = float(input("Введите сторону d прямоугольника: "))

    # Проверка возможности вмещения прямоугольника
    if (a <= c and b <= d) or (a <= d and b <= c):
        print("Входит")
    else:
        print("Не входит")
        
    # 2
    
    # Ввод оценок студента в одну строку через пробел
    grades_input = input("Введите оценки студента через пробел: ")

    # Преобразование строки в список целых чисел
    grades = list(map(int, grades_input.split()))

    # Подсчет количества двоек в списке оценок
    count_twos = grades.count(2)

    # Вывод результата без использования циклов
    print("Отчислен" if count_twos > 1 else "Учится")


def task15():
    a = int(input("Введите ширину форточки (a): "))
    b = int(input("Введите высоту форточки (b): "))
    d = int(input("Введите диаметр головы (d): "))
    print(can_head_pass_through_window(a, b, d))
    def can_head_pass_through_window(a, b, d):
        required_space = d + 2
        if required_space <= a and required_space <= b:
            return "ДА"
        else:
            return "НЕТ"

    # 2
    
    def add_moscow_if_missing(cities_string):
        cities_list = cities_string.split()
        if "Москва" not in cities_list:
            cities_list.append("Москва")
        return cities_list

    # Пример использования:
    cities_string = input("Введите названия городов через пробел: ")
    updated_cities_list = add_moscow_if_missing(cities_string)
    print(updated_cities_list)


def task16():
    def is_valid_email(email):
        if len(email) >= 5 and '@' in email and '.' in email:
            at_index = email.index('@')
            dot_index = email.index('.', at_index)
            if at_index < dot_index:
                return "ДА"
        return "НЕТ"

    # Пример использования:
    email = input("Введите email-адрес: ")
    print(is_valid_email(email))

    # 2
    
    def compute_average(numbers_string):
    # Замена запятых на пробелы и разделение строки на части
        numbers_list = list(map(int, numbers_string.replace(',', ' ').split()))
        # Вычисление среднего арифметического
        average = sum(numbers_list) / len(numbers_list)
        return average

    # Пример использования:
    numbers_string = input("Введите целые числа через пробел или запятую: ")
    print(compute_average(numbers_string))

def task17():
    def find_divisors(n):
        i = 1
        divisors = []
        while i <= n:
            if n % i == 0:
                divisors.append(i)
            i += 1
        return divisors

    # Пример использования:
    n = int(input("Введите натуральное число: "))
    print("Делители числа", n, ":", find_divisors(n))

    # 2
    
    import re

    def replace_multiple_hyphens(url_fragment):
        return re.sub(r'-+', '-', url_fragment)

    # Пример использования:
    url_fragment = input("Введите фрагмент URL-адреса: ")
    print(replace_multiple_hyphens(url_fragment))

def task18():
    def sum_of_digits(n):
        sum_digits = 0
        while n > 0:
            sum_digits += n % 10
            n //= 10
        return sum_digits

    # Пример использования:
    n = int(input("Введите натуральное число: "))
    print("Сумма цифр числа:", sum_of_digits(n))

    # 2
    
    def first_two_cities(cities_string):
        cities_list = cities_string.split()
        cities_iter = iter(cities_list)
        first_city = next(cities_iter, None)
        second_city = next(cities_iter, None)
        return first_city, second_city

    # Пример использования:
    cities_string = input("Введите список городов через пробел: ")
    first_city, second_city = first_two_cities(cities_string)
    print("Первый город:", first_city)
    print("Второй город:", second_city)

def task19():
    def all_cities_longer_than_five(cities_string):
        cities = cities_string.split()
        i = 0
        while i < len(cities):
            if len(cities[i]) <= 5:
                return "НЕТ"
            i += 1
        return "ДА"

    # Пример использования:
    cities_string = input("Введите список городов через пробел: ")
    print(all_cities_longer_than_five(cities_string))

    # 2
    def check_no_touching_ones(matrix):
        def is_valid(i, j):
            return 0 <= i < 5 and 0 <= j < 5
        
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == 1:
                    # Проверка всех соседей
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if (di != 0 or dj != 0) and is_valid(i + di, j + dj) and matrix[i + di][j + dj] == 1:
                                return "НЕТ"
        return "ДА"

    # Пример использования:
    matrix = [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ]

    print(check_no_touching_ones(matrix))


def task20():
    def check_names(names_string):
        names = names_string.split()
        i = 0
        while i < len(names):
            name = names[i].lower()
            if name[0] == name[-1]:
                return "ДА"
            i += 1
        return "НЕТ"

    # Пример использования:
    names_string = input("Введите список имен студентов через пробел: ")
    print(check_names(names_string))

    # 2
    
    def min_bills(n):
        denominations = [64, 32, 16, 8, 4, 2, 1]
        result = []
        for bill in denominations:
            while n >= bill:
                result.append(bill)
                n -= bill
        return result

    # Пример использования:
    n = int(input("Введите натуральное число: "))
    print("Минимальное количество купюр для выплаты суммы:", min_bills(n))

def task21():
    def find_first_square_greater_than_n(n):
        i = 1
        while True:
            if i * i > n:
                return i
            i += 1

    # Пример использования:
    n = int(input("Введите натуральное число: "))
    print("Первое натуральное число, квадрат которого больше", n, ":", find_first_square_greater_than_n(n))

    # 2
    
    def flatten_list(nested_list):
        flattened = []
        for element in nested_list:
            if isinstance(element, list):
                for subelement in element:
                    if isinstance(subelement, list):
                        for subsubelement in subelement:
                            flattened.append(subsubelement)
                    else:
                        flattened.append(subelement)
            else:
                flattened.append(element)
        return flattened

    # Пример использования:
    lst = [1, 2, [True, False, ["a", "ra"]], 3]
    print("Одномерный список:", flatten_list(lst))

def task22():
    def sum_odd_numbers(numbers_string):
        numbers = list(map(int, numbers_string.split()))
        total_sum = 0
        for number in numbers:
            if number % 2 != 0:
                total_sum += number
        return total_sum

    # Пример использования:
    numbers_string = input("Введите целые числа через пробел: ")
    print("Сумма нечетных чисел:", sum_odd_numbers(numbers_string))

    # 2
    
    def check_tic_tac_toe_win(board):
        for row in board:
            if row == ['x', 'x', 'x']:
                return "ДА"
        
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == 'x':
                return "ДА"
        
        if board[0][0] == board[1][1] == board[2][2] == 'x' or board[0][2] == board[1][1] == board[2][0] == 'x':
            return "ДА"
        
        return "НЕТ"

    # Пример использования:
    P = [['x', 'x', 'o'], ['o', 'x', 'x'], ['#', 'x', '#']]
    print(check_tic_tac_toe_win(P))

def task23():
    def check_city_sequence(cities_string):
        cities = cities_string.split()
        for i in range(len(cities) - 1):
            last_char = cities[i][-1].lower()
            if last_char in 'ьъы':
                last_char = cities[i][-2].lower()
            if cities[i+1][0].lower() != last_char:
                return "НЕТ"
        return "ДА"

    # Пример использования:
    cities_string = input("Введите список названий городов через пробел: ")
    print(check_city_sequence(cities_string))

    # 2
    
    def pack_backpack(N):
        items = [["карандаш", 20], ["зеркальце", 100], ["рубашка", 300], ["молоток", 600], ["пила", 400], ["удочка", 1200]]
        items.sort(key=lambda x: x[1], reverse=True)
        packed_items = []
        for item in items:
            if item[1] <= N:
                packed_items.append(item[0])
                N -= item[1]
        return packed_items

    # Пример использования:
    N = int(input("Введите максимальный вес рюкзака: "))
    print("Предметы, которые можно положить в рюкзак:", pack_backpack(N))

def task24():
    import re

    def check_phone_number(phone_number):
        pattern = r'^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$'
        return "ДА" if re.fullmatch(pattern, phone_number) else "НЕТ"

    # Пример использования:
    phone_number = input("Введите номер телефона: ")
    print(check_phone_number(phone_number))
    
    # 2
    
    def digit_iterator(n):
        return (int(digit) for digit in str(n))

    # Пример использования:
    n = int(input("Введите четырехзначное число: "))
    for digit in digit_iterator(n):
        print(digit, end=' ')
    print()


def task25():
    def square_numbers(numbers_string):
        numbers = list(map(int, numbers_string.split()))
        return [num**2 for num in numbers]

    # Пример использования:
    numbers_string = input("Введите целые числа через пробел: ")
    print("Возведенные в квадрат значения:", square_numbers(numbers_string))

    # 2
    
    def calculate_months():
        amount = 1000
        months = 0
        while amount <= 1200:
            amount += amount * 0.02
            months += 1
        return months

    # Пример использования:
    print("Количество месяцев до достижения 1200 рублей:", calculate_months())

def task26():
    def find_min_even(numbers_string):
        numbers = list(map(int, numbers_string.split()))
        min_even = None
        for num in numbers:
            if num % 2 == 0 and (min_even is None or num < min_even):
                min_even = num
        return min_even if min_even is not None else "None"

    # Пример использования:
    numbers_string = input("Введите целые числа через пробел: ")
    print("Наименьшее четное значение:", find_min_even(numbers_string))

    # 2
    
    def check_adjacent_digits(n):
        n_str = str(n)
        for i in range(len(n_str) - 1):
            if n_str[i] == n_str[i + 1]:
                return n_str[i]
        return "НЕТ"

    # Пример использования:
    n = int(input("Введите натуральное число: "))
    print("Результат:", check_adjacent_digits(n))

def task27():
    def absolute_values(numbers_string):
        return [abs(float(num)) for num in numbers_string.split()]

    # Пример использования:
    numbers_string = input("Введите вещественные числа через пробел: ")
    print("Модули введенных чисел:", absolute_values(numbers_string))

    # 2
    
    def flatten_and_reverse(matrix):
        return [elem for row in matrix for elem in row][::-1]

    # Пример использования:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Одномерный список в обратном порядке:", flatten_and_reverse(matrix))

def task28():
    def digits_of_number(n):
        return [int(digit) for digit in str(n)]

    # Пример использования:
    n = int(input("Введите семизначное число: "))
    print("Цифры числа:", ' '.join(map(str, digits_of_number(n))))

    # 2
    
    def form_square_table(numbers_string):
        numbers = list(map(int, numbers_string.split()))
        n = int(len(numbers)**0.5)
        return [numbers[i*n:(i+1)*n] for i in range(n)]

    # Пример использования:
    numbers_string = input("Введите числа через пробел: ")
    print("Квадратная таблица чисел:")
    for row in form_square_table(numbers_string):
        print(row)

def task29():
    def identity_matrix(n):
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    # Пример использования:
    N = int(input("Введите размерность матрицы N: "))
    print("Матрица с единицами по главной диагонали:")
    for row in identity_matrix(N):
        print(row)
        
    # 2
    
    def words_longer_than_three(texts):
        return [[word for word in line.split() if len(word) > 3] for line in texts]

    # Пример использования:
    t = ["– Скажи-ка, дядя, ведь не даром", "Я Python выучил с каналом", "Наместников что раздавал?"]
    print("Преобразованный список:")
    print(words_longer_than_three(t))


def task30():
    def cities_longer_than_five(cities_string):
        return [city for city in cities_string.split() if len(city) > 5]

    # Пример использования:
    cities_string = input("Введите названия городов через пробел: ")
    print("Города длиной более пяти символов:", cities_longer_than_five(cities_string))
    
    # 2
    
    def create_2d_list():
        lines = []
        while True:
            line = input("Введите строку целых чисел через пробел (или пустую строку для завершения): ")
            if not line:
                break
            lines.append(line.split())
        return [[int(num) for num in line] for line in lines]

    # Пример использования:
    print("Двумерный список:")
    print(create_2d_list())


        
def task31():
    n = int(input("Введите натуральное число: "))
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    print(divisors)
    
    # 2
    
    matrix = [[i + j*4 + 1 for i in range(4)] for j in range(4)]
    for row in matrix:
        print(' '.join(map(str, row)))


def task32():
    N = int(input("Введите натуральное число: "))
    matrix = [[i for _ in range(N)] for i in range(N)]
    for row in matrix:
        print(row)
    
    # 2
    
    import math

    a, b = map(float, input("Введите два вещественных значения a и b (a < b): ").split())
    sin_values = [round(math.sin(x), 2) for x in [a + i*0.1 for i in range(int((b - a)/0.1) + 1)]]
    print(sin_values)


def task33():
    numbers = list(map(float, input("Введите список вещественных чисел через пробел: ").split()))
    even_index_values = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
    print(even_index_values)
    
    # 2
    
    cities = input("Введите названия городов: ").split()
    countries = input("Введите названия стран: ").split()
    rivers = input("Введите названия рек: ").split()
    long_words = [word for word in cities + countries + rivers if len(word) > 5]
    print(long_words)


def task34():
    list1 = list(map(int, input("Введите первый список целых чисел: ").split()))
    list2 = list(map(int, input("Введите второй список целых чисел: ").split()))
    sum_list = [list1[i] + list2[i] for i in range(len(list1))]
    print(sum_list)
    
    # 2
    
    d = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [8, 7, 6]]
    reversed_rows = [row for row in d[::-1]]
    print(reversed_rows)


def task35():
    countries = input("Введите названия стран через пробел: ").split()
    countries_with_ro = [country for country in countries if 'ро' in country.lower()]
    print(countries_with_ro)
    
    # 2
    
    t = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [9, 8, 7]], [[0, 1, 2], [-1, -2]]]
    flattened_list = [item for sublist1 in t for sublist2 in sublist1 for item in sublist2]
    print(flattened_list)


def task36():
    a, b = map(float, input("Введите два натуральных числа a и b (a < b): ").split())
    range_list = [round(a + i*0.1, 1) for i in range(int((b - a)/0.1) + 1)]
    print(range_list)
    
    # 2
    
    coordinates = input("Введите строку с координатами точек: ")
    coordinates_list = [[int(coord) for coord in point.split(';')] for point in coordinates.split()]
    print(coordinates_list)


def task37():
    morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ё': '.', 'ж': '...-', 'з': '--..',
         'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.',
         'с': '...', 'т': '-', 'у': '..-', 'ф': '.. .', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-',
         'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-···-'}

    text = input("Введите строку из русских букв: ").lower()
    encoded = ' '.join([morze[char] for char in text])
    print(encoded)
    
    # 2
    
    cities = tuple(input("Введите названия городов через пробел: ").split())
    if "Москва" not in cities:
        cities += ("Москва",)
    print(cities)


def task38():
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 
     'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 
     'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', 
     ' ': '-', '?': '-', '!': '-', ';': '-', ':': '-'}

    text = input("Введите строку с русскими и латинскими буквами: ").lower()
    translated = ''.join([t.get(char, char) for char in text])
    print(translated)
    
    # 2
    
    students = tuple(input("Введите имена студентов через пробел: ").split())
    filtered_students = [name for name in students if "ва" in name]
    print(' '.join(filtered_students))


def task39():
    things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300}
    d = {}

    while True:
        data = input("Введите предмет и вес (или пустую строку для завершения): ")
        if not data:
            break
        item, weight = data.split('=')
        d[item] = int(weight)

    things.update(d)
    print(things)
    
    # 2
    
    commentators = set()

    while True:
        comment = input("Введите комментарий (или пустую строку для завершения): ")
        if not comment:
            break
        name, _ = comment.split(':', 1)
        commentators.add(name.strip())

    print("Число уникальных комментаторов:", len(commentators))


def task40():
    books = {}
    while True:
        data = input("Введите автора и название книги (или пустую строку для завершения): ")
        if not data:
            break
        author, title = data.split(':')
        if author.strip() not in books:
            books[author.strip()] = title.strip()

    print(books)
    
    # 2
    
    cities = tuple(input("Введите названия городов через пробел: ").split())
    filtered_cities = tuple(city for city in cities if city != "Самара")
    print(' '.join(filtered_cities))


def task41():
    # Часть 1
    grades_input = input("Введите оценки студента через пробел: ")
    grades = map(int, grades_input.split())

    grades_count = {grade: list(grades).count(grade) for grade in set(grades)}

    print("Словарь с количеством оценок:", grades_count)
    
    # 2
    
    # Часть 2
    # Ввод списков
    list1 = list(map(int, input("Введите первый список чисел через пробел: ").split()))
    list2 = list(map(int, input("Введите второй список чисел через пробел: ").split()))

    set1 = set(list1)
    set2 = set(list2)

    difference = set1 - set2

    print("Числа, присутствующие в первом списке, но отсутствующие во втором:", ' '.join(map(str, sorted(difference))))


def task42():
    # Часть 1
    numbers_input = input("Введите числа в формате '1;3 4 5;2 4 3 4;1;6 8 10; ...': ")
    groups = numbers_input.split(';')

    figures_dict = {}

    for group in groups:
        items = group.split()
        figure_type = items.pop(0)
        figures_dict[figure_type] = [list(map(int, items))]

    print("Словарь с фигурами и их группами чисел:")
    for key, value in figures_dict.items():
        print(key + ':', value)
        
    # 2
    
    

def task43():
    # Часть 1
    phones_dict = {}

    while True:
        phone_number = input("Введите номер телефона (или пустую строку для завершения): ").strip()
        if phone_number == "":
            break
        country_code = phone_number[:2]
        if country_code not in phones_dict:
            phones_dict[country_code] = []
        phones_dict[country_code].append(phone_number)

    print("Словарь с номерами телефонов по кодам стран:")
    for key, value in phones_dict.items():
        print(key + ':', value)
        
    # 2
    
    # Часть 2
    cities1 = set(input("Введите города первого списка через пробел: ").split())
    cities2 = set(input("Введите города второго списка через пробел: ").split())

    if cities1 <= cities2:
        print("ДА")
    else:
        print("НЕТ")


def task44():
    import math

    # Часть 1
    results = {}

    while True:
        num = int(input("Введите целое число (или 0 для завершения): "))
        if num == 0:
            break
        if num not in results:
            results[num] = round(math.cos(num), 3)
        print(f"Косинус числа {num}:", results[num])
        
    # 2
    
    # Часть 2
    list1 = set(map(int, input("Введите первый список чисел через пробел: ").split()))
    list2 = set(map(int, input("Введите второй список чисел через пробел: ").split()))

    common_elements = sorted(list1 & list2)

    print("Числа, присутствующие в обоих списках:", ' '.join(map(str, common_elements)))


def task45():
    # Часть 1
    def is_odd(num):
        return num % 2 != 0

    cities = input("Введите список городов через пробел: ").split()

    odd_cities = [city for city in cities if len(city) >= 3]

    print("Города длиной не менее трех символов:", odd_cities)
    
    # 2
    
    # Часть 2
    def flatten_list(d):
        flattened = []
        for item in d:
            if isinstance(item, list):
                flattened.extend(flatten_list(item))
            else:
                flattened.append(item)
        return flattened

    d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], [True, [1, -1]]], 7.89]

    flattened_list = flatten_list(d)

    print("Одномерный список из значений элементов списка d:", flattened_list)
    
def task46():
    # Часть 1
    def is_even(num):
        return num % 2 == 0

    while True:
        num = int(input("Введите целое число (1 для выхода): "))
        if num == 1:
            break
        if is_even(num):
            print(num)

    # 2
    
    # Часть 2
    def recursive_sum(numbers):
        if not numbers:
            return 0
        else:
            return numbers[0] + recursive_sum(numbers[1:])

    numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
    sum_result = recursive_sum(numbers)

    print("Сумма введенных значений:", sum_result)

def task47():
    # Часть 1
    def is_odd(num):
        return num % 2 != 0

    numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

    odd_numbers = [num for num in numbers if is_odd(num)]

    print("Список нечетных чисел:", odd_numbers)
    
    # 2
    
    # Часть 2
    def fibonacci_sequence(n):
        if n <= 0:
            return []
        elif n == 1:
            return [1]
        elif n == 2:
            return [1, 1]
        else:
            fib_sequence = [1, 1]
            for i in range(2, n):
                fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
            return fib_sequence

    n = int(input("Введите натуральное число n для последовательности Фибоначчи: "))
    fib_sequence = fibonacci_sequence(n)

    print("Последовательность Фибоначчи:", fib_sequence)


def task48():
    # Часть 1
    word = input("Введите слово RECT или любое другое слово: ")

    if word == "RECT":
        def get_sq(a, b):
            return a * b
    else:
        def get_sq(a, b):
            return 2 * (a + b)

    # Вызов функции
    a = float(input("Введите сторону a: "))
    b = float(input("Введите сторону b: "))

    result = get_sq(a, b)
    print("Результат вычисления:", result)
    
    
    # Часть 2
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    n = int(input("Введите натуральное число n для вычисления факториала: "))
    factorial_result = factorial(n)

    print(f"Факториал числа {n}:", factorial_result)


def task49():
    # Часть 1
    def check_length(city):
        return len(city) >= 3

    cities = input("Введите список городов через пробел: ").split()

    filtered_cities = [city for city in cities if check_length(city)]

    print("Города длиной не менее трех символов:", filtered_cities)
    
    # Часть 2
    def flatten_list(d):
        flattened = []
        for item in d:
            if isinstance(item, list):
                flattened.extend(flatten_list(item))
            else:
                flattened.append(item)
        return flattened

    d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], [True, [1, -1]]], 7.89]

    flattened_list = flatten_list(d)

    print("Одномерный список из значений элементов списка d:", flattened_list)


def task50():
    # Часть 1
    def city_length(city):
        return city, len(city)

    cities = input("Введите список городов через пробел: ").split()

    d = {city: length for city, length in map(city_length, cities)}

    print("Словарь городов с их длинами:")
    for city, length in d.items():
        print(f"{city}: {length}")
        
    # Часть 2
    num = float(input("Введите вещественное число: "))

    absolute = lambda x: abs(x)

    print("Модуль числа:", absolute(num))


    
