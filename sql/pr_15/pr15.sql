-- =========================================================================
-- ПР15. Сквозной сценарий: песочница, переменные, массивы и CSV
-- =========================================================================

-- ЧАСТЬ 1. Переменные (на примере мок-таблицы выдач)
-- Создаем тестовую таблицу для имитации вашей базы проката
DROP TABLE IF EXISTS rentals;
CREATE TABLE rentals (id INTEGER PRIMARY KEY, tool_id INTEGER, deposit INTEGER);
INSERT INTO rentals (tool_id, deposit) VALUES (1, 500), (2, 1000), (3, 1000);

-- Переносимая замена переменной (CTE)
-- В MySQL можно было бы сделать: SET @max_dep = (SELECT MAX(deposit) FROM rentals);
WITH max_dep_cte AS (SELECT MAX(deposit) AS max_d FROM rentals)
SELECT id, tool_id, deposit FROM rentals WHERE deposit = (SELECT max_d FROM max_dep_cte);
-- РЕЗУЛЬТАТ: Выдано 2 строки с залогом 1000.

-- Вторая переменная (количество выдач)
SELECT COUNT(*) AS total_rentals FROM rentals;
-- РЕЗУЛЬТАТ: 3

-- =========================================================================
-- ЧАСТЬ 2. Песочница (перезапускаемый скрипт)
-- =========================================================================
DROP TABLE IF EXISTS demo_tools;
CREATE TABLE demo_tools (
  id            INTEGER PRIMARY KEY,   -- суррогатный ключ
  name          TEXT NOT NULL,
  category      TEXT NOT NULL,
  price_per_day INTEGER NOT NULL
);

INSERT INTO demo_tools (name, category, price_per_day) VALUES
  ('Молоток слесарный',  'ручной',  90),
  ('Отвертка набор',     'ручной',  60),
  ('Дрель ударная',      'электро', 330),
  ('Перфоратор',         'электро', 390),
  ('Пила циркулярная',   'электро', 330),
  ('Стремянка 3 м',      'высота',  120);

DROP TABLE IF EXISTS tools_stage;
CREATE TABLE tools_stage (
  name          TEXT NOT NULL,
  category      TEXT NOT NULL,
  price_per_day INTEGER NOT NULL
);

-- Контрольные проверки (Числа совпадают при 2-м запуске)
-- COUNT = 6, MIN = 60, MAX = 390, AVG = 220.0

-- =========================================================================
-- ЧАСТЬ 3. «Массив»: VALUES, CTE и временная таблица
-- =========================================================================
-- 1. Проверка CTE
WITH batch(name, category, price_per_day) AS (VALUES
  ('Стремянка 2 м',       'высота',  110),
  ('Перфоратор SDS-Plus', 'электро', 420),
  ('Стремянка 3 м',       'высота',  130))
SELECT COUNT(*) AS n, MAX(price_per_day) AS top_price FROM batch;
-- РЕЗУЛЬТАТ: n=3, top_price=420

-- 2. Временная таблица
CREATE TEMP TABLE batch (name TEXT, category TEXT, price_per_day INTEGER);
INSERT INTO batch VALUES
  ('Стремянка 2 м',       'высота',  110),
  ('Перфоратор SDS-Plus', 'электро', 420),
  ('Стремянка 3 м',       'высота',  130);

-- Запрос к массиву (сколько позиций дороже 200)
SELECT COUNT(*) FROM batch WHERE price_per_day > 200;
-- РЕЗУЛЬТАТ: 1

-- Обновление каталога из массива
UPDATE demo_tools
SET price_per_day = (SELECT b.price_per_day FROM batch b WHERE b.name = demo_tools.name)
WHERE EXISTS (SELECT 1 FROM batch b WHERE b.name = demo_tools.name);
-- РЕЗУЛЬТАТ: Обновлена 1 строка (Стремянка 3 м, цена стала 130).

-- =========================================================================
-- ЧАСТЬ 4. Импорт из CSV в staging (Массив <- Табличный файл)
-- =========================================================================
-- Имитация импорта (в реальности выполняется командой .import для SQLite)
-- DELETE FROM tools_stage; (чтобы не дублировать при повторном запуске)
DELETE FROM tools_stage;
INSERT INTO tools_stage (name, category, price_per_day) VALUES
  ('Стремянка 2 м',       'высота',  110),
  ('Перфоратор SDS-Plus', 'электро', 420),
  ('Стремянка 3 м',       'высота',  130);

-- Перенос из staging в каталог с защитой от дублей (NOT EXISTS)
INSERT INTO demo_tools (name, category, price_per_day)
SELECT s.name, s.category, s.price_per_day
FROM tools_stage s
WHERE NOT EXISTS (SELECT 1 FROM demo_tools d WHERE d.name = s.name);
-- РЕЗУЛЬТАТ: Вставлено 2 строки (Стремянка 2 м и Перфоратор SDS-Plus).

-- Итоговый максимум в каталоге
SELECT MAX(price_per_day) FROM demo_tools;
-- РЕЗУЛЬТАТ: 420

-- =========================================================================
-- ЧАСТЬ 5. Выгрузка в CSV (Табличный файл <- Массив/Таблица)
-- =========================================================================
-- Запрос для выгрузки. (В SQLite перед этим: .mode csv, .titles on, .once price_list.csv)
SELECT name, category, price_per_day
FROM demo_tools
ORDER BY category, name;