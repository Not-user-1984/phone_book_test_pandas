from phonebook import PhoneBook
from phonebook_interface import PhoneBookInterface


def main() -> None:
    filename: str = "phonebook.csv"
    phonebook: PhoneBook = PhoneBook(filename)
    interface: PhoneBookInterface = PhoneBookInterface(phonebook)
    interface.run()


if __name__ == "__main__":
    main()
