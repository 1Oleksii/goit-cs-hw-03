from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до моєї бази (мій URI)
client = MongoClient("mongodb+srv://rasilka111:2AKcTcuhfyiCC3XV@cluster0.1btbyw5.mongodb.net/")

db = client.cat_database
collection = db.cats

def create_cat(name, age, features):
    """Створити запис кота"""
    try:
        cat = {"name": name, "age": age, "features": features}
        result = collection.insert_one(cat)
        print(f"Created cat with id {result.inserted_id}")
    except Exception as e:
        print("Error:", e)

def read_all_cats():
    """Вивести всіх котів"""
    try:
        for cat in collection.find():
            print(cat)
    except Exception as e:
        print("Error:", e)

def read_cat_by_name(name):
    """Знайти кота по імені"""
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"No cat named {name}")
    except Exception as e:
        print("Error:", e)

def update_cat_age(name, new_age):
    """Оновити вік кота"""
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print(f"Updated age for {name}")
        else:
            print(f"No cat named {name} to update")
    except Exception as e:
        print("Error:", e)

def add_feature_to_cat(name, feature):
    """Додати нову характеристику коту"""
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.modified_count > 0:
            print(f"Added feature to {name}")
        else:
            print(f"No cat named {name} to update")
    except Exception as e:
        print("Error:", e)

def delete_cat_by_name(name):
    """Видалити кота за іменем"""
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Deleted cat named {name}")
        else:
            print(f"No cat named {name} to delete")
    except Exception as e:
        print("Error:", e)

def delete_all_cats():
    """Видалити всі записи"""
    try:
        result = collection.delete_many({})
        print(f"Deleted {result.deleted_count} cats")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    # Приклади виклику функцій
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    read_all_cats()
    read_cat_by_name("barsik")
    update_cat_age("barsik", 4)
    add_feature_to_cat("barsik", "любить гратися")
    delete_cat_by_name("barsik")
    delete_all_cats()
