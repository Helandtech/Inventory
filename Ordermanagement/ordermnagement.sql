CREATE IF NOT EXISTS DATABASE `orderinventory`;
USE `orderinventory`;

		CREATE TABLE stock (
		    order_id int NOT NULL AUTO_INCREMENT,
		    supply_name text,
		    PRIMARY KEY (`order_id`)
		    );

INSERT INTO stock (supply_name ) VALUES 
('Apple'),
('Orange'),
('Peach'),
('Carrot'),
('Tomatoes'),
('Pear'),
('Water'),
('Beef'),
('Wine'),
('Chocolate'),
('Crisps');


	CREATE TABLE create_order (
		    order_id int NOT NULL AUTO_INCREMENT,
		    orders_name varchar(255) DEFAULT 'Order',
			user_id VARCHAR(255) ,
		    PRIMARY KEY (`order_id`),
            Unique (`user_id`)
		    );

	CREATE TABLE add_product_order (
		    id int NOT NULL AUTO_INCREMENT,
		    product_name text,
		    product_quantity int,
            product_id int,
            status varchar(255) DEFAULT 'DRAFT',
            PRIMARY KEY (`id`)
		    );

