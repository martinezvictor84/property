-- -----------------------------------------------------
-- Table `habi`.`type_interaction`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `habi`.`type_interaction` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `habi`.`interaction`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `habi`.`interaction` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `auth_user_id` INT(11) NOT NULL,
  `property_id` INT(11) NOT NULL,
  `type_interaction_id` INT NOT NULL,
  `create_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `active` TINYINT(1) NULL DEFAULT 1,
  `update_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_interaction_auth_user_idx` (`auth_user_id` ASC),
  INDEX `fk_interaction_property1_idx` (`property_id` ASC),
  INDEX `fk_interaction_type_interaction1_idx` (`type_interaction_id` ASC),
  CONSTRAINT `fk_interaction_auth_user`
    FOREIGN KEY (`auth_user_id`)
    REFERENCES `habi_db`.`auth_user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_interaction_property1`
    FOREIGN KEY (`property_id`)
    REFERENCES `habi_db`.`property` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_interaction_type_interaction1`
    FOREIGN KEY (`type_interaction_id`)
    REFERENCES `habi`.`type_interaction` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

INSERT INTO `habi`.`type_interaction` (`id`, `name`) VALUES (1, 'like');