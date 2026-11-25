-- ================ МЕНЮ БАЗЫ ПРОКАТА ================
-- ПР17: пункты меню = виды; исполнение сверху вниз.
-- 1. СОЗДАТЬ  — пять CREATE VIEW (срезы данных)
-- 2. ПОКАЗАТЬ — SELECT от каждого вида и уточнения
-- 3. НАЙТИ    — проверка актуальности (INSERT + SELECT)
-- 4. ИЗМЕНИТЬ — пересоздание вида с новой колонкой
-- 5. УДАЛИТЬ  — DROP VIEW IF EXISTS (чистка)
-- =====================================================

-- [ПОДГОТОВКА БАЗЫ] (Если база уже есть, этот блок можно пропустить)
DROP TABLE IF EXISTS rentals;
DROP TABLE IF EXISTS tools;
DROP TABLE IF EXISTS clients;

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


-- =====================================================
-- СЕКЦИЯ 1: СОЗДАТЬ (CREATE VIEW)
-- =====================================================
DROP VIEW IF EXISTS v_open_full;
DROP VIEW IF EXISTS v_price;
DROP VIEW IF EXISTS v_open;
DROP VIEW IF EXISTS v_rentals_full;
DROP VIEW IF EXISTS v_client_deposits;

-- 1.1. Пункт «прайс» (проекция: только названия и цены)
CREATE VIEW v_price AS
SELECT name, price_per_day FROM tools;

-- 1.2. Пункт «на руках» (фильтр по NULL: невозвращённые выдачи)
CREATE VIEW v_open AS
SELECT id, client_id, tool_id, rent_date, deposit
FROM rentals WHERE return_date IS NULL;

-- 1.3. Пункт «карточка выдачи» (соединение 3 таблиц)
CREATE VIEW v_rentals_full AS
SELECT r.id, c.name AS client, t.name AS tool,
       r.rent_date, r.return_date, r.deposit
FROM rentals r
JOIN clients c ON r.client_id = c.id
JOIN tools t   ON r.tool_id = t.id;

-- 1.4. Пункт «клиенты в цифрах» (агрегат с GROUP BY)
CREATE VIEW v_client_deposits AS
SELECT c.name, COUNT(r.id) AS rentals_cnt, SUM(r.deposit) AS deposits_total
FROM clients c
LEFT JOIN rentals r ON r.client_id = c.id
GROUP BY c.id, c.name;

-- 1.5. Пункт «меню внутри меню» (вид поверх вида)
CREATE VIEW v_open_full AS
SELECT * FROM v_rentals_full WHERE return_date IS NULL;


-- =====================================================
-- СЕКЦИЯ 2: ПОКАЗАТЬ (SELECT FROM VIEWS)
-- =====================================================
-- Самый дорогой инструмент из прайса
SELECT name, price_per_day FROM v_price ORDER BY price_per_day DESC;

-- Выдачи на руках с именами (сортировка по дате)
SELECT client, tool, rent_date FROM v_open_full ORDER BY rent_date;

-- Клиенты, которые оставили залогов больше 500 руб (уточнение поверх агрегата)
SELECT name, deposits_total FROM v_client_deposits WHERE deposits_total > 500;

-- Список всех видов в базе (оглавление)
SELECT name FROM sqlite_master WHERE type = 'view';


-- =====================================================
-- СЕКЦИЯ 3: НАЙТИ (Проверка актуальности)
-- =====================================================
-- Добавляем новую выдачу (без даты возврата)
INSERT INTO rentals (id, client_id, tool_id, rent_date, return_date, deposit) 
VALUES (9, 3, 3, '2026-11-15', NULL, 500);

-- Проверяем, что вид v_open сразу её увидел (без пересоздания вида)
SELECT * FROM v_open WHERE id = 9;


-- =====================================================
-- СЕКЦИЯ 4: ИЗМЕНИТЬ (ALTER/REPLACE/Пересоздание)
-- =====================================================
-- В SQLite нет ALTER VIEW и CREATE OR REPLACE VIEW.
-- Убедимся в этом (раскомментируйте, чтобы увидеть ошибку):
-- ALTER VIEW v_price AS SELECT name FROM tools; 
-- Ошибка: OperationalError: near "VIEW": syntax error

-- Родной способ SQLite — DROP + CREATE:
DROP VIEW v_price;

-- Пересоздаем вид, дописав новую колонку (category) в конец
CREATE VIEW v_price AS
SELECT name, price_per_day, category FROM tools;

-- Проверяем, что новые данные видны
SELECT * FROM v_price LIMIT 3;


-- =====================================================
-- СЕКЦИЯ 5: УДАЛИТЬ (DROP VIEW)
-- =====================================================
-- Удаляем вид-надстройку, который решили не оставлять
DROP VIEW IF EXISTS v_open_full;

-- Пытаемся удалить его еще раз (без IF EXISTS) — будет ошибка
-- DROP VIEW v_open_full;
-- Ошибка: no such view: v_open_full

-- Правильный безопасный способ:
DROP VIEW IF EXISTS v_open_full;