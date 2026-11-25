username = input("Введіть ім'я користувача: ")
email = input("Введіть електронну адресу: ")
age = input("Введіть вік: ")
password = input("Введіть пароль: ")

errors = []

if not username:
    errors.append("Ім'я користувача не може бути порожнім.")
if username and username[0].isdigit():
    errors.append("Ім'я користувача не може починатися з цифри.")   
if len(username) < 5:
    errors.append("Ім'я користувача повинно містити щонайменше 5 символів.")   
if " " in username:
    errors.append("Ім'я користувача не може містити пробіли.")
    
if not email:
    errors.append("Електронна адреса не може бути порожньою.")
if email.count("@") != 1:
    errors.append("Електронна адреса повинна містити один символ '@'.")
    
if not age:
    errors.append("Вік не може бути порожнім.")
if not age.isdigit():
    errors.append("Вік повинен бути числом.")
if age.isdigit() and int(age) < 16:
    errors.append("Вік повинен бути не меншим за 16 років.")

if not password:
    errors.append("Пароль не може бути порожнім.")
if len(password) < 8:
    errors.append("Пароль повинен містити щонайменше 8 символів.")
if " " in password:
    errors.append("Пароль не може містити пробіли.")
if password and len(set(password)) == 1:
    errors.append("Пароль не може складатися з одного й того ж символа.")
    
if errors:
    print("Помилки при введенні даних:")
    for error in errors:
        print(f"- {error}")
else:
    print("Всі дані введено правильно.")