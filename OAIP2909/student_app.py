import sqlite3

# глобальные переменные для базы
conn = sqlite3.connect('students.db')
cursor = conn.cursor()


def init_db():
    # создание таблицы
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        group_name TEXT,
        grade INTEGER,
        age INTEGER
    )''')
    conn.commit()

    # добавление 5 студентов если база пустая
    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        data = [
            ('Иванов Иван', 'ИСП-101', 5, 19),
            ('Петров Пётр', 'ИСП-101', 4, 20),
            ('Сидоров Алексей', 'ИСП-102', 3, 18),
            ('Смирнова Анна', 'ИСП-102', 5, 19),
            ('Кузнецов Максим', 'ИСП-101', 4, 21)
        ]
        cursor.executemany("INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)", data)
        conn.commit()


def show_all():
    # вывод всех
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    for row in data:
        print(f"ID: {row[0]} | ФИО: {row[1]} | Группа: {row[2]} | Оценка: {row[3]} | Возраст: {row[4]}")


def add_student():
    # добавление нового
    name = input("Введите ФИО: ")
    group = input("Введите группу: ")

    while True:
        try:
            grade = int(input("Введите оценку: "))
            age = int(input("Введите возраст: "))
            break
        except ValueError:
            print("Ошибка! Введите число.")

    cursor.execute("INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)", (name, group, grade, age))
    conn.commit()
    print("Студент добавлен!")


def find_by_group():
    # поиск по группе
    group = input("Введите название группы: ")
    cursor.execute("SELECT * FROM students WHERE group_name = ?", (group,))
    data = cursor.fetchall()
    if not data:
        print("Студентов в такой группе нет.")
    else:
        for row in data:
            print(f"ID: {row[0]} | ФИО: {row[1]} | Оценка: {row[3]}")


def find_by_grade():
    # поиск по оценке
    while True:
        try:
            grade = int(input("Введите оценку для поиска: "))
            break
        except ValueError:
            print("Нужно ввести число!")

    cursor.execute("SELECT * FROM students WHERE grade = ?", (grade,))
    data = cursor.fetchall()
    if not data:
        print("Никого не найдено.")
    else:
        for row in data:
            print(f"ID: {row[0]} | ФИО: {row[1]} | Группа: {row[2]}")


def update_grade():
    # изменение оценки
    show_all()
    while True:
        try:
            sid = int(input("Введите ID студента: "))
            new_grade = int(input("Введите новую оценку: "))
            break
        except ValueError:
            print("Ошибка ввода!")

    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, sid))
    conn.commit()
    print("Оценка изменена!")


def delete_student():
    # удаление студента
    show_all()
    sid = input("Введите ID студента для удаления: ")
    cursor.execute("DELETE FROM students WHERE id = ?", (sid,))
    conn.commit()
    print("Студент удален. Оставшиеся:")
    show_all()


def extra_task():
    # доп задание
    cursor.execute("SELECT grade FROM students")
    grades = cursor.fetchall()
    if not grades:
        print("База пуста.")
        return

    total = 0
    for g in grades:
        total += g[0]
    avg = total / len(grades)
    print(f"Средняя оценка всех студентов: {avg:.2f}")


def main():
    init_db()
    while True:
        print("\n===== УЧЁТ СТУДЕНТОВ =====")
        print("1. Показать всех студентов")
        print("2. Добавить студента")
        print("3. Найти студентов по группе")
        print("4. Найти студентов по оценке")
        print("5. Изменить оценку")
        print("6. Удалить студента")
        print("7. Средняя оценка (доп. задание)")
        print("0. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            show_all()
        elif choice == '2':
            add_student()
        elif choice == '3':
            find_by_group()
        elif choice == '4':
            find_by_grade()
        elif choice == '5':
            update_grade()
        elif choice == '6':
            delete_student()
        elif choice == '7':
            extra_task()
        elif choice == '0':
            print("Выход...")
            break
        else:
            print("Нет такого пункта!")

    # закрытие соединения
    conn.close()


if __name__ == "__main__":
    main()