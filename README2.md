# Завдання 2: Реалізації основних CRUD (Create, Read, Update, Delete) операцій у MongoDB

У цьому завданні реалізовано Python скрипт для роботи з базою даних MongoDB за допомогою бібліотеки PyMongo. Скрипт виконує основні CRUD операції з колекцією документів, що містять інформацію про котів.

🟢 **Структура документа**

Кожен документ має поля:

- `_id`: унікальний ідентифікатор (генерується автоматично),
- `name`: ім'я кота (рядок),
- `age`: вік кота (число),
- `features`: список характеристик кота (масив рядків).

🟢 **Функції скрипта**

- `create_cat(name, age, features)`: додає нового кота до колекції.
- `read_all_cats()`: виводить усі записи котів з бази.
- `read_cat_by_name(name)`: шукає та виводить інформацію про кота за ім'ям.
- `update_cat_age(name, new_age)`: оновлює вік кота за ім'ям.
- `add_feature_to_cat(name, feature)`: додає нову характеристику коту.
- `delete_cat_by_name(name)`: видаляє запис кота за ім'ям.
- `delete_all_cats()`: очищує всю колекцію.

🟢 **Особливості реалізації**

- Для кожної операції передбачена обробка можливих помилок через блоки `try-except`.
- Кожна функція має короткий коментар, що пояснює її призначення.
- Підключення до MongoDB реалізовано через URI з використанням MongoClient.
- Скрипт може працювати як із локальним сервером MongoDB, так і з MongoDB Atlas.