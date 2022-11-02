-- ********************************* Audit History *********************************
-- Name                 Action      Date            Comment
--Bhushan Bapat         Create      10/8/2022

-- *********************************************************************************

-- Table: dbo.UserPassengerDetails

-- DROP TABLE IF EXISTS dbo."UserPassengerDetails";

CREATE TABLE IF NOT EXISTS dbo."UserPassengerDetails"
(
    "passengerId" uuid NOT NULL,
    userid uuid NOT NULL,
    "firstName" character varying(20) COLLATE pg_catalog."default" NOT NULL,
    "middleName" character varying(20) COLLATE pg_catalog."default",
    "lastName" character varying(20) COLLATE pg_catalog."default" NOT NULL,
    "DOB" date NOT NULL,
    "mobileNo" numeric(10,0) NOT NULL,
    "adhaarNo" numeric(12,0),
    "panCardNo" character varying(10) COLLATE pg_catalog."default",
    CONSTRAINT "UserPassengerDetails_pkey" PRIMARY KEY ("passengerId"),
    CONSTRAINT "userPassenger" FOREIGN KEY (userid)
        REFERENCES dbo."User" ("userId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS dbo."UserPassengerDetails"
    OWNER to postgres;
-- Index: fki_userPassenger

-- DROP INDEX IF EXISTS dbo."fki_userPassenger";

CREATE INDEX IF NOT EXISTS "fki_userPassenger"
    ON dbo."UserPassengerDetails" USING btree
    (userid ASC NULLS LAST)
    TABLESPACE pg_default;
