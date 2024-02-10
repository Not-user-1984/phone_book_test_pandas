# phonebook_interface.py

from typing import Dict, Any
import pandas as pd
from phonebook import PhoneBook


class PhoneBookInterface:
    def __init__(self, phonebook: PhoneBook) -> None:
        self.phonebook: PhoneBook = phonebook

    def display_menu(self) -> None:
        print("\nТелефонный справочник:")
        print("1. Показать записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Удалить запись")
        print("6. Выход")

    def display_search_menu(self) -> str:
        print("Выберите поле для поиска:")
        print("1. Фамилия")
        print("2. Имя")
        print("3. Отчество")
        print("4. Организация")
        print("5. Рабочий телефон")
        print("6. Личный телефон")
        choice = input("Выберите поле: ")
        fields = {
            "1": "Фамилия",
            "2": "Имя",
            "3": "Отчество",
            "4": "Организация",
            "5": "Рабочий телефон",
            "6": "Личный телефон"
        }
        return fields.get(choice, None)

    def run(self) -> None:
        while True:
            self.display_menu()
            choice: str = input("Выберите действие: ")
            if choice == "1":
                page_num: int = int(input("Введите номер страницы: "))
                self.phonebook.display_page(page_num)
            elif choice == "2":
                entry: Dict[str, Any] = {
                    "Фамилия": input("Введите фамилию: "),
                    "Имя": input("Введите имя: "),
                    "Отчество": input("Введите отчество: "),
                    "Организация": input("Введите название организации: "),
                    "Рабочий телефон": input("Введите рабочий телефон: "),
                    "Личный телефон": input("Введите личный телефон: ")
                }
                self.phonebook.add_entry(entry)
                print("Запись добавлена.")
            elif choice == "3":
                index: int = int(input("Введите номер записи для редактирования: "))
                new_entry: Dict[str, Any] = {
                    "Фамилия": input("Введите новую фамилию: "),
                    "Имя": input("Введите новое имя: "),
                    "Отчество": input("Введите новое отчество: "),
                    "Организация": input("Введите новое название организации: "),
                    "Рабочий телефон": input("Введите новый рабочий телефон: "),
                    "Личный телефон": input("Введите новый личный телефон: ")
                }
                self.phonebook.edit_entry(index, new_entry)
                print("Запись отредактирована.")
            elif choice == "4":
                field = self.display_search_menu()
                if field:
                    value = input(f"Введите значение для поля '{field}': ")
                    results: pd.DataFrame = self.phonebook.search(field, value)
                    print(results)
                else:
                    print("Неверный выбор поля.")
            elif choice == "5":
                index: int = int(input("Введите номер записи для удаления: "))
                self.phonebook.delete_entry(index)
                print("Запись удалена.")
            elif choice == "6":
                print("Выход.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
