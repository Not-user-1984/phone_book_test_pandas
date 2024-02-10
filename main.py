from typing import Dict, Any
import pandas as pd


class PhoneBook:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self.data: pd.DataFrame = None
        self.load_data()

    def load_data(self) -> None:
        if pd.read_csv(self.filename).empty:
            self.data = pd.DataFrame(columns=["Фамилия", "Имя", "Отчество", "Организация", "Рабочий телефон", "Личный телефон"])
        else:
            self.data = pd.read_csv(self.filename)

    def save_data(self) -> None:
        self.data.to_csv(self.filename, index=False)

    def display_page(self, page_num: int, page_size: int = 5) -> None:
        start_idx: int = page_num * page_size
        end_idx: int = (page_num + 1) * page_size
        page_data: pd.DataFrame = self.data.iloc[start_idx:end_idx]
        print(page_data)

    def add_entry(self, entry: Dict[str, Any]) -> None:
        self.data = pd.concat([self.data, pd.DataFrame([entry])], ignore_index=True)
        self.save_data()

    def edit_entry(self, index: int, new_entry: Dict[str, Any]) -> None:
        self.data.loc[index] = new_entry
        self.save_data()

    def search(self, **kwargs: str) -> pd.DataFrame:
        query: pd.Series = pd.Series(kwargs)
        results: pd.DataFrame = self.data.copy()
        for key, value in query.items():
            if value:
                results = results[results[key] == value]
        return results


class PhoneBookInterface:
    def __init__(self, phonebook: PhoneBook) -> None:
        self.phonebook: PhoneBook = phonebook

    def display_menu(self) -> None:
        print("\nТелефонный справочник:")
        print("1. Показать записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выход")

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
                search_criteria: Dict[str, str] = {}
                search_criteria["Фамилия"] = input("Введите фамилию (пусто для игнорирования): ")
                search_criteria["Имя"] = input("Введите имя (пусто для игнорирования): ")
                search_criteria["Отчество"] = input("Введите отчество (пусто для игнорирования): ")
                search_criteria["Организация"] = input("Введите название организации (пусто для игнорирования): ")
                search_criteria["Рабочий телефон"] = input("Введите рабочий телефон (пусто для игнорирования): ")
                search_criteria["Личный телефон"] = input("Введите личный телефон (пусто для игнорирования): ")
                results: pd.DataFrame = self.phonebook.search(**search_criteria)
                print(results)
            elif choice == "5":
                print("Выход.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")


def main() -> None:
    filename: str = "phonebook.csv"
    phonebook: PhoneBook = PhoneBook(filename)
    interface: PhoneBookInterface = PhoneBookInterface(phonebook)
    interface.run()


if __name__ == "__main__":
    main()
