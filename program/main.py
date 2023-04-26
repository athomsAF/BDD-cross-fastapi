import mysql.connector as MC

def table_delete(cursor):
      for i in ["COMMAND", "COMPOSITION", "SHOP", "CLIENT", "FLOWER", "BOUQUET"]:
            cursor.execute(f"DROP TABLE IF EXISTS {i};")

def table_creation(cursor) -> None:
      cursor.execute("""
                        CREATE TABLE IF NOT EXISTS SHOP (
                        IDSHOP INTEGER NOT NULL AUTO_INCREMENT,
                        NAME VARCHAR(255) UNIQUE NOT NULL,
                        ADRESS VARCHAR(255) NOT NULL,
                        PRIMARY KEY (IDSHOP));
                        """)
      cursor.execute("""
                        CREATE TABLE IF NOT EXISTS CLIENT (
                        IDCLIENT INTEGER NOT NULL AUTO_INCREMENT,
                        NAME VARCHAR(255) NOT NULL,
                        LASTNAME VARCHAR(255) NOT NULL,
                        PHONE_NUMBER VARCHAR(10) NOT NULL,
                        MAIL VARCHAR(255) NOT NULL,
                        PASSWORD VARCHAR(255) NOT NULL,
                        FACTURATION_ADDRESS VARCHAR(255) NOT NULL,
                        CREDIT_CARD_NUMBER VARCHAR(16) NOT NULL,
                        FIDELITY INTEGER(1) DEFAULT 0 CHECK (FIDELITY >= 0 AND FIDELITY <= 2),
                        CONSTRAINT CHK_PHONE_NUMBER CHECK (LENGTH(PHONE_NUMBER) = 10 AND PHONE_NUMBER REGEXP '^[0-9]+$'),
                        CONSTRAINT CHK_MAIL CHECK (MAIL REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+"""+"\\"+""".[a-zA-Z]{2,}$'),
                        PRIMARY KEY (MAIL, PASSWORD),
                        UNIQUE (IDCLIENT)
                        );
                        """)
      cursor.execute("""
                        CREATE TABLE IF NOT EXISTS COMMAND (
                        IDCOMMAND INTEGER NOT NULL AUTO_INCREMENT,
                        IDSHOP INTEGER(8) NOT NULL,
                        IDCLIENT INTEGER(8) NOT NULL,
                        DATE DATE NOT NULL,
                        PRIMARY KEY (IDCOMMAND),
                        FOREIGN KEY (IDSHOP) REFERENCES SHOP(IDSHOP),
                        FOREIGN KEY (IDCLIENT) REFERENCES CLIENT(IDCLIENT));
                  """)
      cursor.execute("""
                  CREATE TABLE IF NOT EXISTS FLOWER (
                        IDFLOWER INTEGER NOT NULL AUTO_INCREMENT,
                        NAME VARCHAR(255) UNIQUE NOT NULL,
                        PRICE INTEGER(3) NOT NULL,
                        QUANTITE INTEGER(3) NOT NULL,
                        PRIMARY KEY (IDFLOWER));
                  """)
      cursor.execute("""
                        CREATE TABLE IF NOT EXISTS BOUQUET (
                        IDBOUQUET INTEGER NOT NULL AUTO_INCREMENT,
                        NAME VARCHAR(255) UNIQUE NOT NULL,
                        PRICE INTEGER(3) NOT NULL,
                        DESCRIPTION VARCHAR(255),
                        CREATION_DATE DATE NOT NULL,
                        PRIMARY KEY (IDBOUQUET));
                  """)
      cursor.execute("""
                        CREATE TABLE IF NOT EXISTS COMPOSITION (
                        IDBOUQUET INTEGER(8) NOT NULL,
                        IDFLOWER INTEGER(8) NOT NULL,
                        QUANTITY INTEGER(3) NOT NULL,
                        FOREIGN KEY (IDBOUQUET) REFERENCES BOUQUET(IDBOUQUET),
                        FOREIGN KEY (IDFLOWER) REFERENCES FLOWER(IDFLOWER));
                        """)