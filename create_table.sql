CREATE TABLE IF NOT EXISTS `addresses` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `address` CHAR(255),
    `date` DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
