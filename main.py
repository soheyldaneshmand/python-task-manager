
import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def show_menu():
    print("\n===== Task Manager =====")
    print("1. Ezafe kardan kar")
    print("2. Namayeshe karha")
    print("3. Hazfe kar")
    print("4. Takmil kar")
    print("5. Khorooj")


def add_task(tasks):
    title = input("Name kar ra vared konid: ")

    if title.strip() == "":
        print("Name kar nemitavanad khali bashad!")
        return

    tasks.append({
        "title": title,
        "completed": False
    })

    save_tasks(tasks)
    print("Kar ba movafaghiat ezafe shod!")


def show_tasks(tasks):
    if not tasks:
        print("Hich kari vojood nadarad.")
        return

    print("\n===== List of Tasks =====")

    for index, task in enumerate(tasks, start=1):
        status = "Anjam shode" if task["completed"] else "Anjam nashode"
        print(f"{index}. {task['title']} - {status}")


def delete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Shomare kar baraye hazf: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Kar '{removed['title']}' hazf shod!")
        else:
            print("Shomare namotabar ast!")

    except ValueError:
        print("Lotfan yek adad vared konid!")


def complete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Shomare kar baraye takmil: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("Kar ba movafaghiat takmil shod!")
        else:
            print("Shomare namotabar ast!")

    except ValueError:
        print("Lotfan yek adad vared konid!")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Entekhab shoma: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            complete_task(tasks)

        elif choice == "5":
            print("Barname be payan resid. Khodahafez!")
            break

        else:
            print("Gozine namotabar ast!")


if __name__ == "__main__":
    main()
