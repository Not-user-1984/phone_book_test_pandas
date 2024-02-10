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
        if self.validate_phone_number(entry["Рабочий телефон"]) and self.validate_phone_number(entry["Личный телефон"]):
            self.data = pd.concat([self.data, pd.DataFrame([entry])], ignore_index=True)
            self.save_data()
        else:
            print("Некорректные номера телефонов. Номер должен содержать только цифры и быть не длиннее 100 символов.")

    def edit_entry(self, index: int, new_entry: Dict[str, Any]) -> None:
        if self.validate_phone_number(new_entry["Рабочий телефон"]) and self.validate_phone_number(new_entry["Личный телефон"]):
            self.data.loc[index] = new_entry
            self.save_data()
        else:
            print("Некорректные номера телефонов. Номер должен содержать только цифры и быть не длиннее 100 символов.")

    def delete_entry(self, index: int) -> None:
        self.data.drop(index, inplace=True)
        self.save_data()

    def validate_phone_number(self, number: str) -> bool:
        """
        Проверка номера телефона на корректность.

        Параметры:
        - number (str): Номер телефона.

        Возвращает:
        - bool: True, если номер корректен, False в противном случае.
        """
        return number.isdigit() and len(number) <= 100

    def search(self, field: str, value: str) -> pd.DataFrame:
        if field in self.data.columns:
            return self.data[self.data[field] == value]
        else:
            print("Неверное поле для поиска.")
            return pd.DataFrame()
