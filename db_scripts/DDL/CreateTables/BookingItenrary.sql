-- Table: dbo.BookingItenrary

-- DROP TABLE IF EXISTS dbo."BookingItenrary";

CREATE TABLE IF NOT EXISTS dbo."BookingItenrary"
(
    "itenraryId" uuid NOT NULL,
    "bookingId" uuid NOT NULL,
    "PNR" character varying COLLATE pg_catalog."default" NOT NULL,
    "from" character varying COLLATE pg_catalog."default" NOT NULL,
    "to" character varying COLLATE pg_catalog."default" NOT NULL,
    "travelDate" date NOT NULL,
    "departureTime" date NOT NULL,
    "arrivalTime" date NOT NULL,
    "journeyType" character varying COLLATE pg_catalog."default" NOT NULL,
    "travelClass" character varying COLLATE pg_catalog."default" NOT NULL,
    "airlineVendor" character varying COLLATE pg_catalog."default" NOT NULL,
    "flightNo" character varying COLLATE pg_catalog."default" NOT NULL,
    "flightType" character varying COLLATE pg_catalog."default" NOT NULL,
    "baseFare" numeric NOT NULL,
    CONSTRAINT "BookingItenrary_pkey" PRIMARY KEY ("itenraryId"),
    CONSTRAINT "bookingItenrary" FOREIGN KEY ("bookingId")
        REFERENCES dbo."UserBookings" ("bookingId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS dbo."BookingItenrary"
    OWNER to postgres;
-- Index: fki_bookingItenrary

-- DROP INDEX IF EXISTS dbo."fki_bookingItenrary";

CREATE INDEX IF NOT EXISTS "fki_bookingItenrary"
    ON dbo."BookingItenrary" USING btree
    ("bookingId" ASC NULLS LAST)
    TABLESPACE pg_default;
