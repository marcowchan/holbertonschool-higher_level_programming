-- Lists all the cities of California in hbtn_0d_usa database.
-- Uses hbtn_0d_usa database.
USE `hbtn_0d_usa`;
-- Lists all the cities of California.
SELECT `id`, `name` FROM `cities`
	WHERE `state_id` IN (
		SELECT `id` FROM `states`
		WHERE `name` = `California`
	)
	ORDER BY `id`;
