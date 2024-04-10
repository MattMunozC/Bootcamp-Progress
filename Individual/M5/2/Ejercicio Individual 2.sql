#DROP DATABASE INV_DB;

CREATE DATABASE INV_DB;
USE INV_DB;

CREATE TABLE user_db(
	user_id int PRIMARY KEY,
    RUT varchar(255),
    DV char,
    name varchar(255),
    surname varchar(255),
    registry_date date
);
CREATE TABLE client_db(
	client_id int PRIMARY KEY,
    user_id int,
    foreign key (user_id) REFERENCES user_db(user_id)
);
CREATE TABLE employee(
	employee_id int PRIMARY KEY,
    user_id int,
    foreign key (user_id) REFERENCES user_db(user_id)
);
CREATE TABLE category(
	 category_id int PRIMARY KEY,
     name_cat varchar(255)
);
CREATE TABLE brand(
	brand_id int PRIMARY KEY,
    brand_name varchar(255)
);

CREATE TABLE product(
	product_id int PRIMARY KEY,
    SKU int,
    category_id int,
    brand_id int,
    name_product varchar(255),
    price int,
    register_id int,
    foreign key (register_id) REFERENCES employee(employee_id),
    foreign key (category_id) REFERENCES category(category_id),
    foreign key (brand_id) REFERENCES brand(brand_id)
);

CREATE TABLE selling_order(
	order_id int PRIMARY KEY,
    total int,
    iva int,
    client_id int,
    seller int,
    foreign key (client_id) REFERENCES client_db(client_id),
    foreign key (seller) REFERENCES employee(employee_id)
);
CREATE TABLE status_order(
	status_id int PRIMARY KEY,
    status_name varchar(255)
);
CREATE TABLE sending_order(
	sending_id int PRIMARY KEY,
    order_id int,
    status_order int,
    direction varchar(255),
    delivery_date date,
    sender int,
    foreign key (sender) REFERENCES employee(employee_id),
    foreign key (status_order) REFERENCES status_order(status_id)
);
CREATE TABLE selling_order_sub(
	detail_id int PRIMARY KEY,
    order_id int,
    product_id int,
    quantity int,
    foreign key (order_id) REFERENCES buying_order(order_id),
    foreign key (product_id) REFERENCES product(product_id)
);
CREATE TABLE buying_order(
	buying_id int PRIMARY KEY,
    buyer int,
    total int,
    foreign key (buyer) REFERENCES employee(employee_id)
);
CREATE TABLE buying_order_sub(
	detail_id int PRIMARY KEY,
    order_id int,
    product_id int,
    quantity int,
    foreign key (order_id) REFERENCES buying_order(order_id),
    foreign key (product_id) REFERENCES product(product_id)
);
CREATE TABLE inventory(
	inventory_id int PRIMARY KEY,
    product_id int,
    quantity int,
    foreign key (product_id) REFERENCES product(product_id)
);