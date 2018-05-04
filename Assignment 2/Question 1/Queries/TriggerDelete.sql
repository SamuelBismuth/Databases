CREATE DEFINER=`root`@`localhost` TRIGGER `before_delete_patients` BEFORE DELETE
ON Queue FOR EACH ROW

BEGIN
	UPDATE Queue_Summery
	SET pastient_num = pastient_num - 1
	WHERE doctor_id 
    IN (
		SELECT Qu_Re.doctor_id
		FROM Queue_Reserved AS Qu_Re
		WHERE (
        OLD.queue_id = Qu_Re.queue_id 
        AND 
        OLD.time BETWEEN CONCAT(CAST(Queue_Summery.date AS char), ' 00:00:00') AND CONCAT(CAST(Queue_Summery.date AS char), ' 23:59:59')
        )
    );
END