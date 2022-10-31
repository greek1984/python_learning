
from import_contact import import_contact
from export_contact import export_contact
from print_contact import print_contact
from search_number import search_number

def mess():
    print("Здравствуйте!")

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    etc = input("Примечание: ")
    return [last_name, first_name, phone_number, etc]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def path():
    print("Выбор действия:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_contact(input_data(), sep)
    elif ch == '2':
        data = export_contact()
        print_contact(data)
    else:
        word = input("Введите данные для поиска: ")
        data = export_contact()
        item = search_number(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
            print("-"*85)
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
        else:
            print("Данные не обнаружены")