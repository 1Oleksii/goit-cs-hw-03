-- 1. Отримати всі завдання певного користувача
SELECT * FROM tasks WHERE user_id = 1;

-- 2. Вибрати завдання зі статусом 'new'
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- 3. Оновити статус завдання
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1;

-- 4. Користувачі без завдань
SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

-- 5. Додати нове завдання
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('New Task', 'Some description', 1, 1);

-- 6. Завдання, які не завершено
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

-- 7. Видалити завдання
DELETE FROM tasks WHERE id = 1;

-- 8. Знайти користувачів з певною поштою
SELECT * FROM users WHERE email LIKE '%@example.com';

-- 9. Оновити імʼя користувача
UPDATE users SET fullname = 'Updated Name' WHERE id = 1;

-- 10. Кількість завдань по статусах
SELECT s.name, COUNT(t.id) FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.name;

-- 11. Завдання користувачів із доменом пошти
SELECT t.* FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';

-- 12. Завдання без опису
SELECT * FROM tasks WHERE description IS NULL;

-- 13. Користувачі + завдання у статусі 'in progress'
SELECT u.fullname, t.title FROM users u
JOIN tasks t ON u.id = t.user_id
WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress');

-- 14. Користувачі і кількість їхніх завдань
SELECT u.fullname, COUNT(t.id) FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;
