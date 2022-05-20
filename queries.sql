/* View */

CREATE VIEW forestation
AS
SELECT f.*, 
        l.total_area_sq_mi * 2.59 AS total_area_sqkm,
        r.region,
        r.income_group,
        f.forest_area_sqkm / (l.total_area_sq_mi * 2.5) * 100  AS forest_percentage
FROM forest_area f
JOIN land_area l
ON f.country_code = l.country_code
AND f.year = l.year
JOIN regions r
ON r.country_code = l.country_code;


/* Global Situation */

-- a. What was the total forest area (in sq km) of the world in 1990?

SELECT forest_area_sqkm
FROM forestation
WHERE year = '1990' AND region = 'World';
--41282694.9

-- b. What was the total forest area (in sq km) of the world in 2016?

SELECT forest_area_sqkm
FROM forestation
WHERE year = '2016' AND region = 'World';
--39958245.9

-- c. What was the change (in sq km) in the forest area of the world from 1990 to 2016?

SELECT forest_area_sqkm - (SELECT forest_area_sqkm
                           FROM forestation
                           WHERE (year = '2016' AND region = 'World'))
        AS forest_area_difference
FROM forestation
WHERE (year = '1990' AND region = 'World');

--1324449

-- d. What was the percent change in forest area of the world between 1990 and 2016?

SELECT (forest_area_sqkm - (SELECT forest_area_sqkm
                           FROM forestation
                           WHERE (year = '2016' AND region = 'World')))
        / forest_area_sqkm * 100
        AS forest_area_difference
FROM forestation
WHERE year = '1990' AND region = 'World'

-- 3.20824258980244


-- e. If you compare the amount of forest area lost between 1990 and 2016, to which country's total area in 2016 is it closest to?



/* Regional Outlook */

-- a. What was the percent forest of the entire world in 2016? Which region had the highest pecent forest in 2016, and which had the lowest, to 2 decimal places?

SELECT region,
       year,
       SUM(forest_area_sqkm) / SUM(total_area_sqkm) * 100
       AS percent_forest
FROM forestation
WHERE year = '2016'
GROUP BY region, year
ORDER BY percent_forest;

-- World: 31.37; high: Latin America 46.16 lowest: Middle East 2.06

-- b. What was the percent forest of the entire world in 1990? Which region had the highest pecent forest in 1990, and which had the lowest, to 2 decimal places?

SELECT region,
       year,
       SUM(forest_area_sqkm) / SUM(total_area_sqkm) * 100
       AS percent_forest
FROM forestation
WHERE year = '1990'
GROUP BY region, year
ORDER BY percent_forest;

--World: 32.42; highest: Latin America 32.42; Lowest: Middle East 1.77

-- c. Which regions of the world decreased in forest area from 1990 to 2016?

WITH t1 AS (
        SELECT region, year,
         SUM(forest_area_sqkm) / SUM(total_area_sqkm) * 100
         AS percent_forest
        FROM forestation
        WHERE year = '1990'
        GROUP BY region, year),
t2 AS (SELECT region, year,
        SUM(forest_area_sqkm) / SUM(total_area_sqkm) * 100
        AS percent_forest
       FROM forestation
       WHERE year = '2016'
       GROUP BY region, year)
SELECT t1.region,
       t1.percent_forest AS percent_forest_1990,
       t2.percent_forest AS percent_forest_2016,
       CASE WHEN (t2.percent_forest - t1.percent_forest) <= 0
            THEN 'decrease' ELSE 'increase' END AS change
FROM t1
JOIN t2
ON t2.region = t1.region
ORDER BY change;

--Sub-Saharan Africa 30.67 -> 28.78; Latin America & Caribb 51.09 -> 46.16

/* Country-level detail */


