-- Create a table called Product with the following columns: 
CREATE TABLE Product (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    description TEXT,
    PRIMARY KEY (id)
)

-- Create a inventory log that tracks the inventory of a product over time.
CREATE TABLE InventoryLog (
    id INT NOT NULL AUTO_INCREMENT,
    productId INT NOT NULL,
    quantity INT NOT NULL,
    createdDate DATETIME NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (productId) REFERENCES Product(id)
)

-- Create a table that track the sales records of a product.
CREATE TABLE SalesRecord (
    id INT NOT NULL AUTO_INCREMENT,
    productId INT NOT NULL,
    quantity INT NOT NULL,
    createdDate DATETIME NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (productId) REFERENCES Product(id)
)
