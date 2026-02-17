import json
import os

FILE_NAME = 'projects.json'


# Загрузка данных
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        return json.load(f)


# Сохранение данных
def save_data(data):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# 1. Показать проекты
def show_projects():
    data = load_data()
    if not data:
        print("\n Проектов нет")
        return
    print("\n Созданные проекты:")
    for i, proj in enumerate(data):
        print(f"{i + 1}. {proj['name']} | Статус: {proj['status']}")


# 2. Создать проект
def create_project():
    name = input("\nВведите название проекта: ")
    if not name:
        print("Название не может быть пустым!")
        return
    data = load_data()
    data.append({
        "name": name,
        "status": "Планирование",
        "tasks": []
    })
    save_data(data)
    print(f"Проект '{name}' создан")


# 3. Добавить задачу
def add_task():
    data = load_data()
    if not data:
        print("\nСначала нужно создать проект")
        return

    show_projects()
    try:
        idx = int(input("\nВведите номер проекта: ")) - 1
        if 0 <= idx < len(data):
            task = input("Введите название задачи: ")
            data[idx]['tasks'].append({"task": task, "done": False})
            save_data(data)
            print("Задача добавлена")
        else:
            print("Такого проекта не существует")
    except ValueError:
        print("Требуется ввести число")


# 4. Показать задачи в проекте
def show_tasks():
    data = load_data()
    if not data:
        print("\nПусто")
        return

    show_projects()
    try:
        idx = int(input("\nВведите номер проекта для просмотра задач: ")) - 1
        if 0 <= idx < len(data):
            print(f"\nЗадачи в проекте '{data[idx]['name']}':")
            if not data[idx]['tasks']:
                print("Задачи отсутствуют")
            for i, t in enumerate(data[idx]['tasks']):
                status = "Выполнено" if t['done'] else "В процессе"
                print(f"  {i + 1}. {status} {t['task']}")
        else:
            print("Такого проекта не существует")
    except ValueError:
        print("Требуется ввести число")


# 5. Изменение статуса проекта
def change_status():
    data = load_data()
    if not data:
        print("\nСначала создайте проект")
        return

    show_projects()
    try:
        idx = int(input("\nВведите номер проекта: ")) - 1
        if 0 <= idx < len(data):
            print("\nДоступные статусы:")
            print("1. Планирование")
            print("2. В процессе")
            print("3. Готов")
            choice = input("Выберите номер статуса: ")
            statuses = {"1": "Планирование", "2": "В процессе", "3": "Готов"}
            if choice in statuses:
                data[idx]['status'] = statuses[choice]
                save_data(data)
                print(f"Статус обновлён на '{statuses[choice]}'")
            else:
                print("Неверный выбор.")
        else:
            print("Такого проекта не существует")
    except ValueError:
        print("Требуется ввести число.")


# 6. Изменить статус задачи (Выполнено/Не выполнено)
def toggle_task_status():
    data = load_data()
    if not data:
        print("\nСначала создайте задачу")
        return

    show_projects()
    try:
        idx = int(input("\nВведите номер проекта: ")) - 1
        if 0 <= idx < len(data):
            # Показываем задачи
            print(f"\nЗадачи в проекте '{data[idx]['name']}':")
            if not data[idx]['tasks']:
                print("Задачи отсутствуют")
                return

            for i, t in enumerate(data[idx]['tasks']):
                status = "Выполнено" if t['done'] else "В процессе"
                print(f"  {i + 1}. {status} {t['task']}")

            # Выбор задачи
            task_idx = int(input("\nВведите номер задачи, чтобы изменить статус: ")) - 1
            if 0 <= task_idx < len(data[idx]['tasks']):
                # Меняем статус на противоположный
                current = data[idx]['tasks'][task_idx]['done']
                data[idx]['tasks'][task_idx]['done'] = not current
                save_data(data)

                new_status = "Выполнено" if not current else "Отменено"
                print(f"Статус задачи изменён")
            else:
                print("Такой задачи не существует")
        else:
            print("Такого проекта не существует")
    except ValueError:
        print("Требуется ввести число")


# Меню
def main():
    while True:
        print("\n--- Меню управления проектами ---")
        print("1. Показать проекты")
        print("2. Создать проект")
        print("3. Добавить задачу")
        print("4. Показать задачи")
        print("5. Изменить статус проекта")
        print("6. Изменить статус задачи")
        print("0. Выход")

        choice = input("\nВаш выбор: ")

        if choice == '1':
            show_projects()
        elif choice == '2':
            create_project()
        elif choice == '3':
            add_task()
        elif choice == '4':
            show_tasks()
        elif choice == '5':
            change_status()
        elif choice == '6':
            toggle_task_status()
        elif choice == '0':
            print("\nЗавершение работы...")
            break
        else:
            print("Такой команды не существует, попробуйте ещё раз.")


if __name__ == "__main__":
    main()
