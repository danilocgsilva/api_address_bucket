CREATE TABLE IF NOT EXISTS `tests_results` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `success` BIT(8),
    `address_id` INT(11) NOT NULL,
    `date` DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE `tests_results` ADD CONSTRAINT `address_id` FOREIGN KEY (`address_id`) REFERENCES `addresses` (`id`);
