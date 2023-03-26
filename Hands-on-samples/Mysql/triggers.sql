CREATE TABLE employee(  
    name varchar(45) NOT NULL,    
    occupation varchar(35) NOT NULL,    
    working_date date,  
    working_hours varchar(10)  
);  

INSERT INTO employee VALUES    
('Robin', 'Scientist', '2020-10-04', 12),  
('Warner', 'Engineer', '2020-10-04', 10),  
('Peter', 'Actor', '2020-10-04', 13),  
('Marco', 'Doctor', '2020-10-04', 14),  
('Brayden', 'Teacher', '2020-10-04', 12),  
('Antonio', 'Business', '2020-10-04', 11); 

-- DELIMITER //  
-- Create Trigger before_insert_empworkinghours   
-- BEFORE INSERT ON employee FOR EACH ROW  
-- BEGIN  
-- IF NEW.working_hours < 0 THEN SET NEW.working_hours = 0;  
-- END IF;  
-- END //  

DELIMITER //
CREATE TRIGGER before_insert_empworkinghours
BEFORE INSERT ON employee FOR EACH ROW
BEGIN
IF NEW.working_hours < 0 THEN SET NEW.working_hours = 0;
END IF;
END //
DELIMITER //

INSERT INTO employee VALUES('prathiksha','Developer','2020-10-04',-10);

DELIMITER //
CREATE TRIGGER before_update_occupation
BEFORE UPDATE ON employee FOR EACH ROW
BEGIN 
	IF occupation='Actor' THEN SET NEW.working_hours = 20;
END IF;
END //
DELIMITER //
    
UPDATE employee SET occupation = 'Actor' WHERE name = 'Warner' ;
use python;
select * from employee;

select name, working_hours from (select * from employee order by working_hours desc limit 2) as emp order by working_hours limit 1; 
