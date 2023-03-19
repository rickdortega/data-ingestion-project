-- A view from the join of the `properties` table and the `parkscores` table showing all properties 
-- showing all properties where we can know the park score based on the common columns:
--  + parkscores.park
--  + properties.map_label

CREATE VIEW properties_and_ratings AS 
	SELECT *
	FROM parkscores p 
	INNER JOIN properties p2 ON p.park = p2.map_label
	WHERE p2.objectid IS NOT NULL
