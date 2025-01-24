CREATE TABLE `addresses` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `address` CHAR(255),
    `date` DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;