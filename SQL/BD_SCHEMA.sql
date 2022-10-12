-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           PostgreSQL 14.4, compiled by Visual C++ build 1914, 64-bit
-- OS do Servidor:               
-- HeidiSQL Versão:              12.0.0.6468
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Copiando estrutura para tabela app.auth
CREATE SCHEMA IF NOT EXISTS app;

CREATE TABLE IF NOT EXISTS auth (
	"cpf" VARCHAR(11) NOT NULL,
	"nome" VARCHAR NOT NULL,
	"cep" VARCHAR(8) NOT NULL,
	"usuario" VARCHAR NOT NULL,
	"email" VARCHAR NOT NULL,
	"senha" VARCHAR NOT NULL,
	PRIMARY KEY ("cpf")
);

-- Exportação de dados foi desmarcado.

--Sujeito a mudanças
--*CREATE TABLE IF NOT EXISTS "user_data" (
--);

CREATE TABLE IF NOT EXISTS control (
	"ID" VARCHAR NOT NULL,
	"Status" BOOLEAN NOT NULL,
	PRIMARY KEY("ID")
);

-- Exportação de dados foi desmarcado.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
