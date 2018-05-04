CREATE DEFINER=`root`@`localhost` PROCEDURE `physical_entry`(in patientName varchar(40))
BEGIN

DECLARE q_id INT;

SET @q_id = (
SELECT Qu_Re.queue_id  
FROM Queue_Reserved as Qu_Re 
JOIN Patients AS Pa
ON Pa.pastient_name = patientName
WHERE
Qu_Re.pastient_id = Pa.pastient_id);

IF(@q_id > 0)

	THEN

	INSERT INTO my_Hospital.Queue (queue_id, time)
	VALUES (@q_id , now());

END IF ;

END