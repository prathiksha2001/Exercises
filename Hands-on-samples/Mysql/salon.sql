CREATE TABLE customers (
    coustomer_id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY
);

Alter table appointments add column customer_id int;

ALTER TABLE customers RENAME COLUMN coustomer_id TO customer_id;

ALTER TABLE appointments ADD CONSTRAINT FOREIGN KEY(customer_id) REFERENCES customers(customer_id);

ALTER TABLE appointments ADD COLUMN  service_id INT;

ALTER TABLE appointments ADD CONSTRAINT FOREIGN KEY(service_id) REFERENCES services(service_id);

ALTER TABLE customers ADD COLUMN phone VARCHAR(13) UNIQUE;

ALTER TABLE customers ADD COLUMN name varchar(30);

ALTER TABLE services ADD COLUMN name varchar(30);

ALTER TABLE appointments ADD COLUMN time VARCHAR(10);

SHOW TABLES;
DESC customers;
DESC appointments;
DESC services;

INSERT INTO services(name) VALUES("Hair styling");

select * from services;
INSERT INTO services(name) VALUES("coloring");

INSERT INTO services(name) VALUES("waxing");

INSERT INTO services(name) VALUES("straightening");

select * from services;

desc customers;

INSERT INTO customers(name, phone) VALUES ("pratham", "444-555-6666");

INSERT INTO customers(name, phone) VALUES ("shaals", "222-555-6666");

INSERT INTO customers(name, phone) VALUES ("bob", "444-999-6666");

select * from customers;

desc appointments;

INSERT INTO appointments(customer_id, service_id, time) VALUES(2,1,"10:30 PM");
INSERT INTO appointments(customer_id, service_id, time) VALUES(1,3,"7:30 PM");
INSERT INTO appointments(customer_id, service_id, time) VALUES(3,4,"11:30 AM");

SELECT 
    c.name, s.name, time, phone
FROM
    customers c
        INNER JOIN
    appointments a ON c.customer_id = a.customer_id
        INNER JOIN
    services s ON s.service_id = a.service_id;
    
CREATE DATABASE hello;
DROP DATABASE hello;