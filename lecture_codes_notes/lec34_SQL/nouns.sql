create table
  nouns as
select "dog" as phrase union
select "cat" union
select "bird";

select subject.phrase || " chased " || object.phrase
from nouns as subject, nouns as object
where subject.phrase <> object.phrase;
