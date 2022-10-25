-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema panel_de_los_pensamientos
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `panel_de_los_pensamientos` ;

-- -----------------------------------------------------
-- Schema panel_de_los_pensamientos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `panel_de_los_pensamientos` DEFAULT CHARACTER SET utf8mb3 ;
USE `panel_de_los_pensamientos` ;

-- -----------------------------------------------------
-- Table `panel_de_los_pensamientos`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `panel_de_los_pensamientos`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL DEFAULT NULL,
  `last_name` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(100) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `panel_de_los_pensamientos`.`pensamientos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `panel_de_los_pensamientos`.`pensamientos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(255) NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_pensamientos_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_pensamientos_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `panel_de_los_pensamientos`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `panel_de_los_pensamientos`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `panel_de_los_pensamientos`.`likes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `pensamiento_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_likes_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_likes_pensamientos1_idx` (`pensamiento_id` ASC) VISIBLE,
  CONSTRAINT `fk_likes_pensamientos1`
    FOREIGN KEY (`pensamiento_id`)
    REFERENCES `panel_de_los_pensamientos`.`pensamientos` (`id`),
  CONSTRAINT `fk_likes_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `panel_de_los_pensamientos`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 15
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
