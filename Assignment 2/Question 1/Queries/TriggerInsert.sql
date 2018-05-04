CREATE DEFINER=`root`@`localhost` TRIGGER `before_insert_patients` AFTER INSERT
ON Queue FOR EACH ROW

BEGIN
	DECLARE doctor INT;
	IF(date(NEW.time) 
    IN (
		SELECT Qu_Su.date
		FROM Queue_Summery AS Qu_Su
		JOIN Queue_Reserved AS Qu_Re
		WHERE (
		NEW.queue_id = Qu_Re.queue_id
		AND
		Qu_Su.doctor_id = Qu_Re.doctor_id))
    )
    THEN
	UPDATE Queue_Summery
	SET pastient_num = pastient_num + 1
	WHERE doctor_id 
    IN (
		SELECT Qu_Re.doctor_id
		FROM Queue_Reserved AS Qu_Re
		WHERE (
        NEW.queue_id = Qu_Re.queue_id 
        AND 
        NEW.time BETWEEN CONCAT(CAST(Queue_Summery.date AS char), ' 00:00:00') AND CONCAT(CAST(Queue_Summery.date AS char), ' 23:59:59')
        )
    );
    ELSE
        SET @doctor = (SELECT doctor_id FROM Queue_Reserved AS Qu_Re WHERE (new.queue_id = Qu_Re.queue_id));
		INSERT INTO `my_Hospital`.`Queue_Summery` (`doctor_id`, `date`, `pastient_num`) VALUES (@doctor, DATE(NEW.time), '1');

    END IF;
END