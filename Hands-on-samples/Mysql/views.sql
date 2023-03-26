-- use python;
-- select * from customers;
-- -- Insert into customers(name,address) values('Jerry', 'Idly'),('Alex','Orange Island'),('Chinchan','China'),('Gladys','China');


-- CREATE VIEW customer_info 
-- AS
-- 	SELECT name, address FROM customers;

select  * from customer_info order by address LIMIT 5 OFFSET 5get_customer_address_by_name;