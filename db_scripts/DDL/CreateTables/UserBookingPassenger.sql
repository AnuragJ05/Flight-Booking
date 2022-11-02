-- ********************************* Audit History *********************************
-- Name                 Action      Date            Comment
--Bhushan Bapat         Create      10/8/2022

-- *********************************************************************************

-- Table: dbo.UserBookingPassenger

-- DROP TABLE IF EXISTS dbo."UserBookingPassenger";

CREATE TABLE IF NOT EXISTS dbo."UserBookingPassenger"
(
    id uuid NOT NULL,
    "bookingId" uuid NOT NULL,
    "passengerId" uuid NOT NULL,
    "seatNo" character varying COLLATE pg_catalog."default",
    CONSTRAINT "UserBookingPassenter_pkey" PRIMARY KEY (id),
    CONSTRAINT "bookingPassenger" FOREIGN KEY ("passengerId")
        REFERENCES dbo."UserPassengerDetails" ("passengerId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "fk_userBooking" FOREIGN KEY ("bookingId")
        REFERENCES dbo."UserBookings" ("bookingId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS dbo."UserBookingPassenger"
    OWNER to postgres;
-- Index: fki_bookingPassenger

-- DROP INDEX IF EXISTS dbo."fki_bookingPassenger";

CREATE INDEX IF NOT EXISTS "fki_bookingPassenger"
    ON dbo."UserBookingPassenger" USING btree
    ("passengerId" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: fki_fk_userBookingPassenger

-- DROP INDEX IF EXISTS dbo."fki_fk_userBookingPassenger";

CREATE INDEX IF NOT EXISTS "fki_fk_userBookingPassenger"
    ON dbo."UserBookingPassenger" USING btree
    ("bookingId" ASC NULLS LAST)
    TABLESPACE pg_default;
