-- ********************************* Audit History *********************************
-- Name                 Action      Date            Comment
--Bhushan Bapat         Create      10/8/2022

-- *********************************************************************************

-- Table: dbo.UserBookings

-- DROP TABLE IF EXISTS dbo."UserBookings";

CREATE TABLE IF NOT EXISTS dbo."UserBookings"
(
    "bookingId" uuid NOT NULL,
    userid uuid NOT NULL,
    "bookingDate" date NOT NULL,
    "bookingStatus" character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "UserBookings_pkey" PRIMARY KEY ("bookingId"),
    CONSTRAINT "fk_userBookngId" FOREIGN KEY (userid)
        REFERENCES dbo."User" ("userId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS dbo."UserBookings"
    OWNER to postgres;
-- Index: fki_fk_userBookngId

-- DROP INDEX IF EXISTS dbo."fki_fk_userBookngId";

CREATE INDEX IF NOT EXISTS "fki_fk_userBookngId"
    ON dbo."UserBookings" USING btree
    (userid ASC NULLS LAST)
    TABLESPACE pg_default;
