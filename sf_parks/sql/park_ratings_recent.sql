--Shows the most recent ratings for each park based on most recent `park_id`

SELECT p1.park_id, p1.psa, p1.park, p1.fq, p1.score 
from parkscores p1 
inner join
	(SELECT park, max(park_id) as max_id
	 FROM parkscores p
	 GROUP BY park
	 ) p2 ON p1.park_id = p2.max_id
