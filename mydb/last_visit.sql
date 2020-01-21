DELIMITER $$
CREATE DEFINER=`root`@`localhost` FUNCTION `last_visit`(AID int) RETURNS date
BEGIN
	declare last_date date;
	select Appointments.Date into last_date from Appointments
	join Animals on Animals.AnimalID = Appointments.Animals_AnimalID
	where AnimalID = AID
	order by Appointments.Date desc
	limit 1;
	return last_date;
RETURN 1;
END$$
DELIMITER ;
