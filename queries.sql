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

