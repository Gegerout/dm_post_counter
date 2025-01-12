def generate_truth_tables(input_n):
    """
    Генерирует все возможные таблицы истинности для указанного числа переменных

    :param input_n: Число переменных в логической функции
    :return: Генератор, возвращающий таблицы истинности
    """
    num_tables = 1 << (1 << input_n)
    for i in range(num_tables):
        truth_table = []
        for j in range(1 << input_n):
            truth_table.append((i >> j) & 1)
        yield truth_table


def is_t0(truth_table):
    """
    Проверяет, является ли функция сохраняющей 0

    :param truth_table: Таблица истинности функции
    :return: True, если функция T0, иначе False
    """
    return truth_table[0] == 0


def is_t1(truth_table):
    """
    Проверяет, является ли функция сохраняющей 1

    :param truth_table: Таблица истинности функции
    :return: True, если функция T1, иначе False
    """
    return truth_table[-1] == 1


def is_self_dual(truth_table):
    """
    Проверяет, является ли функция самодвойственной

    :param truth_table: Таблица истинности функции
    :return: True, если функция самодвойственная, иначе False
    """
    size = len(truth_table)
    for i in range(size // 2):
        if truth_table[i] == truth_table[-i - 1]:
            return False
    return True


def is_monotone(truth_table, input_n):
    """
    Проверяет, является ли функция монотонной

    :param truth_table: Таблица истинности функции
    :param input_n: Число переменных в функции
    :return: True, если функция монотонная, иначе False
    """
    size = 1 << input_n
    for i in range(size):
        for j in range(size):
            if (i & j) == i:
                if truth_table[j] < truth_table[i]:
                    return False
    return True


def walsh_transform(f):
    """
    Применяет преобразование Уолша к набору значений функции

    :param f: Список значений функции
    :return: Преобразованный список
    """
    size = len(f)
    result = f[:]
    step = 1
    while step < size:
        for i in range(0, size, 2 * step):
            for j in range(step):
                a = result[i + j]
                b = result[i + j + step]
                result[i + j] = a + b
                result[i + j + step] = a - b
        step *= 2
    return result


def is_linear(truth_table):
    """
    Проверяет, является ли функция линейной

    :param truth_table: Таблица истинности функции
    :return: True, если функция линейная, иначе False
    """
    walsh = walsh_transform([(-1) ** x for x in truth_table])
    return all(abs(x) == len(truth_table) or x == 0 for x in walsh)


def classify_post_classes(input_n):
    """
   Подсчитывает количество всех булевых функций для каждой конфигурации классов Поста

    :param input_n: Число переменных в логической функции
    :return: Словарь, где ключи — это кортежи с классификацией, а значения — количество функций в этом классе
    """
    cur_classifications = {}

    for truth_table in generate_truth_tables(input_n):
        t0 = is_t0(truth_table)
        t1 = is_t1(truth_table)
        self_dual = is_self_dual(truth_table)
        monotone = is_monotone(truth_table, input_n)
        linear = is_linear(truth_table)

        properties = []
        if t0:
            properties.append("T0")
        if t1:
            properties.append("T1")
        if self_dual:
            properties.append("S")
        if monotone:
            properties.append("M")
        if linear:
            properties.append("L")

        cur_class_signature = tuple(properties)
        if cur_class_signature not in cur_classifications:
            cur_classifications[cur_class_signature] = 0
        cur_classifications[cur_class_signature] += 1

    return cur_classifications


if __name__ == "__main__":
    n = int(input("Введите количество переменных (n): "))
    classifications = classify_post_classes(n)

    print("\nКлассификация Поста и количество функций:")
    print("+" + "-" * 38 + "+" + "-" * 12 + "+")
    print("| {:<36} | {:<10} |".format("Классификация", "Количество"))
    print("+" + "-" * 38 + "+" + "-" * 12 + "+")
    for class_signature, count in classifications.items():
        if class_signature:
            signature_str = ", ".join(class_signature)
        else:
            signature_str = "Не принадлежат ни одному классу"
        print("| {:<36} | {:<10} |".format(signature_str, count))
    print("+" + "-" * 38 + "+" + "-" * 12 + "+")
