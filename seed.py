from faker import Faker
import psycopg2
import random
from dotenv import load_dotenv
import os

fake = Faker()

# Завантаження змінних із .env
load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cur = conn.cursor()

# Додати статуси
statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cur.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT DO NOTHING;", (status,))

# Додати користувачів
user_ids = []
for _ in range(10):
    fullname = fake.name()
    email = fake.unique.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s) RETURNING id;", (fullname, email))
    user_ids.append(cur.fetchone()[0])

# Додати завдання
for _ in range(30):
    title = fake.sentence(nb_words=4)
    description = fake.paragraph() if random.choice([True, False]) else None
    status_id = random.randint(1, 3)
    user_id = random.choice(user_ids)
    cur.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);",
        (title, description, status_id, user_id)
    )

conn.commit()
cur.close()
conn.close()
print("Дані успішно додано!")