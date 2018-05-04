SELECT P.pastient_name, QR.queue_time

FROM 

my_Hospital.Patients AS P

INNER JOIN
my_Hospital.Queue_Reserved AS QR
ON 
P.pastient_id = QR.pastient_id
AND 
QR.doctor_id = 1 #Check if this manipulation should done in java or sql. (here is an example).

ORDER BY(QR.Queue_time);






