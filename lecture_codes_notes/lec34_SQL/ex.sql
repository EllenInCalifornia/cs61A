create table cities as 
select 38 as latitude, 122 as longitude, "berkeley" as name union
select 42, 71, "cambridge" union
select 45, 93, "Min" union
select 33, 117, "san diego" union
select 26, 80, "Miami" union
select 90, 0, "North Pole";

create table cold as 
select name from cities where latitude >= 43;

create table distances as 
select a.name as first, b.name as second,
60*(b.latitude - a.latitude) as distance 
from cities as a, cities as b;


