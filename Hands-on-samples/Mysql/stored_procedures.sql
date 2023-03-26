use python;
DELIMITER //
CREATE PROCEDURE get_customer_info()
BEGIN 
	SELECT * FROM customers;
END //
DELIMITER ;

CALL get_customer_info()

-- parameter with stored procedures

DELIMITER //
CREATE PROCEDURE get_customer_address_by_name(c_name VARCHAR(255))
BEGIN 
	SELECT address FROM customers WHERE name = c_name;
END //
DELIMITER ;

CALL get_customer_address_by_name('Chinchan')
