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

SELECT (f1.forest_area_sqkm - f2.forest_area_sqkm)
       AS forest_area_difference
FROM forestation f1
JOIN forestation f2
ON f1.country_name = f2.country_name
WHERE f1.year = '1990' AND f2.year = '2016' AND f1.region = 'World';

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
        
SELECT country_name, total_area_sqkm
FROM forestation
WHERE year = '2016' 
 AND total_area_sqkm < (
        SELECT ABS(f1.forest_area_sqkm - f2.forest_area_sqkm)
         AS forest_area_difference
        FROM forestation f1
        JOIN forestation f2
        ON f1.country_name = f2.country_name
        WHERE f1.year = '1990' 
         AND f2.year = '2016' 
         AND f1.region = 'World'
)
ORDER BY 2 DESC
LIMIT 1;

--Peru 1279999.9891


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

-- a. Which 5 countries saw the largest amount decrease in forest area from 1990 to 2016? What was the difference in forest area for each?

WITH t1 AS (
        SELECT country_name, year,
         SUM(forest_area_sqkm)
         AS total_forest_area
        FROM forestation
        WHERE year = '1990' AND region != 'World'
        GROUP BY 1, year),
t2 AS (SELECT country_name, year,
        SUM(forest_area_sqkm)
        AS total_forest_area
       FROM forestation
       WHERE year = '2016' AND region != 'World'
       GROUP BY 1, year)
SELECT t1.country_name,
       t1.total_forest_area AS forest_area_1990,
       t2.total_forest_area AS forest_area_2016,
       t1.total_forest_area - t2.total_forest_area
       AS forest_area_difference
FROM t1
JOIN t2
ON t2.country_name = t1.country_name
WHERE t1.total_forest_area IS NOT NULL
	AND t2.total_forest_area IS NOT NULL
ORDER BY forest_area_difference DESC
LIMIT 5;

--Brazil 541510; Indonesia 282193.9844; Myanmar	107234.0039; Nigeria 106506.00098; Tanzania 102320.

-- b. Which 5 countries saw the largest percent decrease in forest area form 1990 to 2016? What was the percent change to 2 decimal places for each?

WITH t1 AS (
        SELECT country_name, year,
         SUM(forest_area_sqkm)
         AS total_forest_area
        FROM forestation
        WHERE year = '1990' AND region != 'World'
        GROUP BY 1, year),
t2 AS (SELECT country_name, year,
        SUM(forest_area_sqkm)
        AS total_forest_area
       FROM forestation
       WHERE year = '2016' AND region != 'World'
       GROUP BY 1, year)
SELECT t1.country_name,
       (t1.total_forest_area - t2.total_forest_area)
        / t1.total_forest_area * 100
        AS percent_change
FROM t1
JOIN t2
ON t2.country_name = t1.country_name
WHERE t1.total_forest_area IS NOT NULL
	AND t2.total_forest_area IS NOT NULL
ORDER BY 2 DESC
LIMIT 5;

--Togo 75.44, Nigeria 61.79, Uganda 59.12, Mauritania 46.74, Honduras 45.03.

-- c. If countries were grouped by percent forestation in quartiles, which group had the most countries in it in 2016?

WITH t1 AS (SELECT country_name,
		percent_forestation,
            CASE WHEN percent_forestation <= 25 THEN '1st'
            WHEN percent_forestation <= 50 THEN '2nd'
            WHEN percent_forestation <= 75 THEN '3rd'
            ELSE '4th' END AS quartiles
            FROM (SELECT country_name,
                   (forest_area_sqkm / total_area_sqkm) * 100
                   AS percent_forestation
                  FROM forestation
                  WHERE year = '2016' AND region != 'World'
                   AND forest_area_sqkm IS NOT NULL
                   AND total_area_sqkm IS NOT NULL
                  GROUP BY 1, 2) AS t2
            WHERE percent_forestation IS NOT NULL
            GROUP BY 1, 2)
SELECT quartiles, COUNT(*)
FROM t1
GROUP BY 1
ORDER BY 1;

--group 1 < 25%

-- d. List all of the countries that were in the 4th quartile (percent forest > 75%) in 2016.

WITH t1 AS (SELECT country_name,
                percent_forestation,
            CASE WHEN percent_forestation <= 25 THEN '1st'
            WHEN percent_forestation <= 50 THEN '2nd'
            WHEN percent_forestation <= 75 THEN '3rd'
            ELSE '4th' END AS quartiles
            FROM (SELECT country_name,
                   (forest_area_sqkm / total_area_sqkm) * 100
                   AS percent_forestation
                  FROM forestation
                  WHERE year = '2016' AND region != 'World'
                   AND forest_area_sqkm IS NOT NULL
                   AND total_area_sqkm IS NOT NULL
                  GROUP BY 1, 2) AS t2
            WHERE percent_forestation IS NOT NULL
            GROUP BY 1, 2)
SELECT country_name
FROM t1
WHERE quartiles = '4th'
GROUP BY 1
ORDER BY 1;

--American Samoa, Gabon, Guyana, Lao PDR, Micronesia Fed. Sts., Palau Seychelles, Solomon Islands, Suriname.

-- e. How many countries had a percent forestation higher than the United States in 2016?

SELECT country_name,
       (forest_area_sqkm / total_area_sqkm) * 100
       AS percent_forestation
       FROM forestation
       WHERE year = '2016'
        AND region != 'World'
        AND ((forest_area_sqkm / total_area_sqkm) * 100) > (
                SELECT (forest_area_sqkm / total_area_sqkm) * 100
                AS percent_forestation
                FROM forestation
                WHERE year = '2016' AND country_name = 'United States'
)
        AND forest_area_sqkm IS NOT NULL
        AND total_area_sqkm IS NOT NULL;

-- 94

