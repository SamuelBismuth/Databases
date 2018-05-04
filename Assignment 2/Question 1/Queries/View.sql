CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `new_view` AS
    SELECT 
        `Patients`.`pastient_name` AS `name`
    FROM
        ((`Patients`
        JOIN `Queue_Reserved` `Qu_Re` ON ((`Qu_Re`.`pastient_id` = `Patients`.`pastient_id`)))
        JOIN `Queue` `Qu` ON ((`Qu`.`queue_id` = `Qu_Re`.`queue_id`)))
    ORDER BY TIMESTAMPDIFF(MINUTE,
        `Qu_Re`.`queue_time`,
        `Qu`.`time`) DESC
    LIMIT 10