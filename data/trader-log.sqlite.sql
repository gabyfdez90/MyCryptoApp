BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "transactions" (
	"id"	INTEGER,
	"date"	TEXT NOT NULL,
	"time"	TEXT NOT NULL,
	"currency_from"	TEXT NOT NULL,
	"quantity_from"	REAL NOT NULL,
	"currency_to"	TEXT NOT NULL,
	"quantity_to"	REAL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "transactions" VALUES (1,'"2022-10-22"','"10:55:34"','"EUR"',100.0,'"ETH"',2.0);
INSERT INTO "transactions" VALUES (2,'"2022-11-27"','"21:35:23"','"ETH"',1.0,'"BTC"',0.8);
COMMIT;
