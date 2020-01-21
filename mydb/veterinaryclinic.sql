delimiter $$
create function last_visit(AID int) returns DATE
begin

	declare last_date date;
	select appointments.date into last_date from appointments
	join animals on animals.AnimalID = appointments.Animals_AnimalID
	where AnimalID = AID
	order by appointments.date desc
	limit 1;
	return last_date;
end;
$$
-- create procedure new_visit 
-- (in appointment_date date, 
-- in appointment_status varchar(20),
-- in appointment_details varchar(20),
-- in vet int,
-- in animal int)
-- begin
-- insert into appointments (date, status, details, vets_vetid, animals_animalid)
-- values (appointment_date, appointment_status, appointment_details, vet, animal);
-- end;