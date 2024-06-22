-- 1) 
Select distinct city from station where left(city,1) in ('a', 'e', 'i', 'o', 'u') and right(city,1) in ('a', 'e', 'i', 'o', 'u')


-- 2) 
Select MAX(POPULATION) - MIN(POPULATION) As Diff from CITY;


-- 3) 
WITH data AS(
SELECT
MIN(LAT_N) AS x1,
MAX(LAT_N) AS x2,
MIN(LONG_W) AS y1,
MAX(LONG_W) AS y2
FROM station)
SELECT ROUND(SQRT(POWER((x1 - x2),2) + POWER((y1 - y2),2)),4)
FROM data


-- 4) 
SELECT ROUND(LAT_N, 4) FROM (
SELECT ROW_NUMBER() OVER(ORDER BY LAT_N) as "ID_R", LAT_N FROM STATION ORDER BY LAT_N ) as S WHERE S.ID_R = (SELECT (COUNT(LAT_N) + 1 )/ 2 FROM STATION);


-- 5) 
Select c.name from 
city as c inner join country as y 
on c.countrycode= y.code 
where continent='Africa'


-- 6)
Select c.name from 
city as c inner join country as y 
on c.countrycode= y.code 
where continent='Africa'


-- 7)
SELECT 
CASE
  WHEN Grade >= 8 THEN Name
  ELSE NULL
END AS Name, Grade, Marks 
FROM Students INNER JOIN Grades 
ON Students.Marks BETWEEN Grades.Min_Mark AND Grades.Max_Mark 
ORDER BY Grade DESC, Name ASC, Marks ASC


-- 8) 
SELECT c.hacker_id, d.name
FROM Difficulty a JOIN Challenges b ON a.difficulty_level = b. difficulty_level  
JOIN Submissions  c ON c.challenge_id = b.challenge_id 
JOIN Hackers  d ON d.hacker_id  = c.hacker_id 
WHERE c.score = a.score
GROUP BY c.hacker_id, d.name
HAVING COUNT(c.challenge_id) > 1
ORDER BY COUNT(c.challenge_id) DESC, c.hacker_id ASC;


-- 9) 
SELECT w.id, wp.age, w.coins_needed, w.power
FROM wands w
JOIN wands_property wp 
ON w.code = wp.code
JOIN (
    SELECT wp1.age, MIN(w1.coins_needed) AS min_coins_needed, w1.power
    FROM wands w1
    JOIN wands_property wp1
    ON w1.code = wp1.code
    WHERE wp1.is_evil = 0
    GROUP BY wp1.age, w1.power
) mc 
ON w.power = mc.power AND wp.age = mc.age AND w.coins_needed = mc.min_coins_needed 
WHERE wp.is_evil = 0
ORDER BY w.power DESC, wp.age DESC;


-- 10)
select h.hacker_id, h.name, sum(max_score) as total_score from ( 
select hacker_id, max(score) as max_score from Submissions group by hacker_id, challenge_id ) 
s left join Hackers h on s.hacker_id = h.hacker_id 
group by hacker_id, name 
having total_score >0 
order by total_score desc, hacker_id asc;