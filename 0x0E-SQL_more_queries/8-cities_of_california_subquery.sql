-- Lists all the cities of California in hbtn_0d_usa database.
-- Lists all the cities of California.
SELECT `id`, `name` FROM `cities`
	WHERE `state_id` IN (
		SELECT `id` FROM `states`
		WHERE `name` = "California"
	);
