-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema esquema_usuarios
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `esquema_usuarios` ;

-- -----------------------------------------------------
-- Schema esquema_usuarios
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_usuarios` ;
USE `esquema_usuarios` ;

-- -----------------------------------------------------
-- Table `esquema_usuarios`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_usuarios`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) COLLATE 'utf8mb3_bin' NULL DEFAULT NULL,
  `apellido` VARCHAR(45) COLLATE 'utf8mb3_bin' NULL DEFAULT NULL,
  `correo_electronico` VARCHAR(45) COLLATE 'utf8mb3_bin' NULL DEFAULT NULL,
  `contraseña` VARCHAR(200) COLLATE 'utf8mb3_bin' NULL DEFAULT NULL,
  `creado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `actualizado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 13;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
