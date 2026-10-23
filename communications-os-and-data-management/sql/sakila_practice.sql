-- Practice queries on the Sakila sample database (MySQL 8.0)
-- One example for each clause. Run each statement on its own.
USE sakila;

-- SELECT
SELECT first_name, last_name FROM actor;

-- ORDER BY (sort; DESC = high to low)
SELECT title, rental_rate FROM film ORDER BY rental_rate DESC, title ASC;

-- WHERE (filter rows)
SELECT title, length FROM film WHERE length > 180;

-- SELECT DISTINCT (remove duplicates)
SELECT DISTINCT rating FROM film;

-- AND (both conditions must be true)
SELECT title FROM film WHERE rating = 'PG' AND length < 90;

-- OR combined with AND (parentheses control the order)
SELECT title, rating, rental_rate FROM film
WHERE (rating = 'G' OR rating = 'PG') AND rental_rate = 0.99;

-- IN (match any value in a list) and IN with a subquery
SELECT title FROM film WHERE rating IN ('G', 'PG');
SELECT title FROM film
WHERE film_id IN (SELECT film_id FROM film_category WHERE category_id = 1);

-- BETWEEN (inclusive range)
SELECT title, length FROM film WHERE length BETWEEN 60 AND 90;
SELECT payment_id, customer_id, staff_id FROM payment
WHERE payment_id NOT BETWEEN 1 AND 5 ORDER BY customer_id;

-- LIKE (pattern: % = any characters, _ = exactly one character)
SELECT title FROM film WHERE title LIKE 'ACADEMY%';
SELECT last_name FROM actor WHERE last_name LIKE '%SON';

-- LIMIT (cap the number of rows)
SELECT title, length FROM film ORDER BY length DESC LIMIT 10;

-- IS NULL (NULL is not a value; = NULL never matches)
SELECT rental_id, rental_date FROM rental WHERE return_date IS NULL LIMIT 10;

-- ---- Extra practice (own wording, corrected versions) ----
-- Actors with a given first name
SELECT * FROM actor WHERE first_name = 'SCARLETT';
-- How many distinct actor last names?
SELECT COUNT(DISTINCT last_name) FROM actor;
-- Last names used by exactly one actor / more than one actor
SELECT last_name FROM actor GROUP BY last_name HAVING COUNT(*) = 1;
SELECT last_name FROM actor GROUP BY last_name HAVING COUNT(*) > 1;
-- Actor who appears in the most films
SELECT a.actor_id, a.first_name, a.last_name, COUNT(*) AS film_count
FROM actor a JOIN film_actor fa ON fa.actor_id = a.actor_id
GROUP BY a.actor_id, a.first_name, a.last_name
ORDER BY film_count DESC LIMIT 1;
-- Copies of one film at store 1 that are NOT currently rented out
SELECT i.inventory_id
FROM inventory i JOIN film f ON f.film_id = i.film_id
WHERE f.title = 'ACADEMY DINOSAUR' AND i.store_id = 1
  AND NOT EXISTS (SELECT 1 FROM rental r
                  WHERE r.inventory_id = i.inventory_id AND r.return_date IS NULL);
-- Due date of a rental = rental date + the film's rental duration
SELECT r.rental_id, r.rental_date,
       DATE_ADD(r.rental_date, INTERVAL f.rental_duration DAY) AS due_date
FROM rental r
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
ORDER BY r.rental_id DESC LIMIT 1;
-- Average film length overall, and by category
SELECT AVG(length) FROM film;
SELECT c.name, AVG(f.length) AS avg_length
FROM film f JOIN film_category fc ON fc.film_id = f.film_id
JOIN category c ON c.category_id = fc.category_id
GROUP BY c.name ORDER BY avg_length DESC;
-- Categories longer than the overall average
SELECT c.name, AVG(f.length) AS avg_length
FROM film f JOIN film_category fc ON fc.film_id = f.film_id
JOIN category c ON c.category_id = fc.category_id
GROUP BY c.name
HAVING AVG(f.length) > (SELECT AVG(length) FROM film)
ORDER BY avg_length DESC;
