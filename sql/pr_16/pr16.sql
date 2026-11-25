-- =========================================================================
-- ПР16. Массивы строк, ввод-вывод CSV и сверка загрузки
-- =========================================================================

-- ШАГ 0. Подготовка базы (из методички)
DROP TABLE IF EXISTS rentals;
DROP TABLE IF EXISTS rentals_archive;
DROP TABLE IF EXISTS tools;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS tools_import;
DROP TABLE IF EXISTS tools_import_t;
DROP TABLE IF EXISTS stage_tools;

CREATE TABLE clients (id INTEGER PRIMARY KEY, name TEXT NOT NULL, phone TEXT);
CREATE TABLE tools (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, category TEXT NOT NULL, price_per_day REAL NOT NULL);
CREATE TABLE rentals (id INTEGER PRIMARY KEY, client_id INTEGER NOT NULL, tool_id INTEGER NOT NULL, rent_date TEXT NOT NULL, return_date TEXT, deposit REAL NOT NULL);

INSERT INTO clients (id, name, phone) VALUES
  (1, 'Иванов Пётр', '+7 912 000-11-22'), (2, 'Смирнова Анна', NULL),
  (3, 'Кузнецов Пётр', '+7 913 111-22-33'), (4, 'Орлова Мария', '+7 914 222-33-44'), (5, 'Волков Игорь', NULL);

INSERT INTO tools (id, name, category, price_per_day) VALUES
  (1, 'Дрель ударная', 'Электроинструмент', 350), (2, 'Шуруповёрт', 'Электроинструмент', 280),
  (3, 'Перфоратор', 'Электроинструмент', 420), (4, 'Молоток', 'Ручной инструмент', 90),
  (5, 'Стамеска', 'Ручной инструмент', 60), (6, 'Рубанок', 'Ручной инструмент', 120),
  (7, 'Уровень лазерный', 'Измерение', 240), (8, 'Рулетка', 'Измерение', 40);

INSERT INTO rentals (id, client_id, tool_id, rent_date, return_date, deposit) VALUES
  (1, 1, 1, '2026-10-05', '2026-10-09', 1000), (2, 2, 4, '2026-10-12', '2026-10-14', 300),
  (3, 3, 3, '2026-10-18', '2026-10-25', 1200), (4, 1, 6, '2026-10-20', '2026-10-27', 400),
  (5, 4, 2, '2026-11-02', NULL, 800), (6, 5, 7, '2026-11-05', NULL, 600),
  (7, 2, 8, '2026-11-08', '2026-11-10', 150), (8, 3, 1, '2026-11-12', NULL, 1000);

-- =========================================================================
-- ЧАСТЬ 1. Многострочный VALUES
-- =========================================================================
-- 1. Батч из трёх клиентов
INSERT INTO clients (id, name, phone) VALUES
  (6, 'Фёдорова Ольга', '+7 915 333-44-55'), (7, 'Морозов Данил', NULL), (8, 'Николаева Вера', '+7 916 444-55-66');

-- До вставки: COUNT(*) = 5. После: COUNT(*) = 8.
-- SELECT id, name FROM clients ORDER BY id DESC LIMIT 3; (вернет 8, 7, 6).

-- 2. Ломаем кортеж (раскомментируйте, чтобы увидеть ошибку)
-- INSERT INTO clients (id, name) VALUES (9, 'Тестов Тест', '+7 900 000-00-00');
-- Ошибка SQLite: "3 values for 2 columns". Вставка отменяется, COUNT = 8.

-- 3. Свой батч из 3 выдач (две с NULL в return_date)
INSERT INTO rentals (id, client_id, tool_id, rent_date, return_date, deposit) VALUES
  (9, 1, 2, '2026-11-15', NULL, 800), (10, 4, 3, '2026-11-16', NULL, 1200), (11, 2, 4, '2026-11-17', '2026-11-18', 300);

-- До: COUNT = 8, SUM = 5450.0. После: COUNT = 11, SUM = 7750.0.

-- =========================================================================
-- ЧАСТЬ 2. INSERT ... SELECT
-- =========================================================================
CREATE TABLE rentals_archive (id INTEGER PRIMARY KEY, client_id INTEGER NOT NULL, tool_id INTEGER NOT NULL, rent_date TEXT NOT NULL, return_date TEXT, deposit REAL NOT NULL);

-- 1. Перенос октябрьских выдач в архив
INSERT INTO rentals_archive (id, client_id, tool_id, rent_date, return_date, deposit)
SELECT id, client_id, tool_id, rent_date, return_date, deposit
FROM rentals WHERE return_date IS NOT NULL AND rent_date < '2026-11-01';

-- В архиве: 4 строки, SUM = 2900.0.

DELETE FROM rentals WHERE return_date IS NOT NULL AND rent_date < '2026-11-01';

-- В rentals осталось: 7 строк, SUM = 4850.0.
-- Проверка: 4850.0 + 2900.0 = 7750.0 (до переноса было 7750.0).

-- 2. Условие "закрытые выдачи ноября"
SELECT COUNT(*) FROM rentals WHERE return_date IS NOT NULL AND rent_date >= '2026-11-01';
-- Вернет 1 (выдача id 11).

-- 3. INSERT ... SELECT ... UNION ALL в tools
INSERT INTO tools (id, name, category, price_per_day)
  SELECT 9, 'Степлер строительный', 'Ручной инструмент', 110
  UNION ALL
  SELECT 10, 'Тестер напряжения', 'Электроинструмент', 150;
-- COUNT(tools) = 10.

-- =========================================================================
-- ЧАСТЬ 3. Временная таблица (Staging)
-- =========================================================================
CREATE TEMP TABLE stage_tools (s_id INTEGER PRIMARY KEY, t_id INTEGER NOT NULL, name TEXT NOT NULL, category TEXT NOT NULL, price_per_day REAL NOT NULL);

INSERT INTO stage_tools (s_id, t_id, name, category, price_per_day) VALUES
  (1, 11, 'Ключ разводной', 'Ручной инструмент', 70), (2, 12, 'Ключ разводной', 'Ручной инструмент', 70),
  (3, 13, 'Генератор', 'Электроинструмент', 900), (4, 14, 'Лобзик', 'Электроинструмент', 310),
  (5, 15, 'Перфоратор', 'Электроинструмент', 420), (6, 16, 'Теодолит', 'Измерение', 500);

-- Проверки: COUNT(*) = 6, COUNT(DISTINCT name) = 5.
-- Дубль: 'Ключ разводной' | 2.

-- Попытка переноса с дублем (раскомментируйте, чтобы увидеть ошибку)
-- INSERT INTO tools (id, name, category, price_per_day) SELECT t_id, name, category, price_per_day FROM stage_tools WHERE name NOT IN (SELECT name FROM tools);
-- Ошибка: UNIQUE constraint failed: tools.name. Вставка откатывается, COUNT = 10.

-- Чистим дубль и переносим
DELETE FROM stage_tools WHERE s_id = 2;
INSERT INTO tools (id, name, category, price_per_day)
SELECT t_id, name, category, price_per_day FROM stage_tools WHERE name NOT IN (SELECT name FROM tools);
-- Вставлено 4 строки. COUNT(tools) = 14.

-- =========================================================================
-- ЧАСТЬ 4. Ввод-вывод CSV
-- =========================================================================
CREATE TABLE tools_import (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price_per_day REAL NOT NULL);

-- ВНИМАНИЕ: Для этого шага в консоли SQLite используются команды:
-- .headers on
-- .mode csv
-- .once tools.csv
-- SELECT id, name, category, price_per_day FROM tools ORDER BY id;
-- .import --csv --skip 1 tools.csv tools_import
-- Для имитации в скрипте мы просто копируем данные:
INSERT INTO tools_import SELECT * FROM tools;

-- Сверка:
SELECT COUNT(*), SUM(price_per_day) FROM tools;        -- 14 | 6640.0
SELECT COUNT(*), SUM(price_per_day) FROM tools_import; -- 14 | 6640.0

-- Ловушка с заголовком
CREATE TEMP TABLE tools_import_t (id TEXT, name TEXT, category TEXT, price_per_day TEXT);
INSERT INTO tools_import_t SELECT * FROM tools;
INSERT INTO tools_import_t VALUES ('id', 'name', 'category', 'price_per_day');
-- SELECT COUNT(*) FROM tools_import_t; -- 15 (заголовок стал строкой)
-- DELETE FROM tools_import_t WHERE id = 'id'; -- Чистим, снова 14.

-- =========================================================================
-- ЧАСТЬ 5. Агрегатные функции
-- =========================================================================
-- 1. Карточка rentals (после переноса в архив, с учетом новых выдач)
SELECT COUNT(*), SUM(deposit), AVG(deposit), MIN(deposit), MAX(deposit) FROM rentals;
-- 7 | 4850.0 | 692.85 | 150.0 | 1200.0

-- 2. Сверка переноса
SELECT 
  (SELECT COUNT(*) FROM rentals) + (SELECT COUNT(*) FROM rentals_archive) AS rows_total,
  (SELECT SUM(deposit) FROM rentals) + (SELECT SUM(deposit) FROM rentals_archive) AS deposit_total;
-- 11 | 7750.0

-- 3. COUNT(*) vs COUNT(column)
SELECT COUNT(*), COUNT(phone) FROM clients;
-- 8 | 5 (у Смирновой и Морозова телефон NULL)

-- 4. Группировка
SELECT category, COUNT(*), ROUND(AVG(price_per_day), 2), MIN(price_per_day), MAX(price_per_day)
FROM tools GROUP BY category ORDER BY category;
-- Измерение: 3, 260.0, 40.0, 500.0
-- Ручной: 5, 90.0, 60.0, 120.0
-- Электро: 6, 401.67, 150.0, 900.0