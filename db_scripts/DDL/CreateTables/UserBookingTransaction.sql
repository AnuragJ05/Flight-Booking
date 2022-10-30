-- Table: dbo.UserBookingTransaction

-- DROP TABLE IF EXISTS dbo."UserBookingTransaction";

CREATE TABLE IF NOT EXISTS dbo."UserBookingTransaction"
(
    "bookingId" uuid NOT NULL,
    "transactionId" uuid NOT NULL,
    "totalAmount" numeric NOT NULL,
    "CGST" numeric NOT NULL,
    "SGST" numeric NOT NULL,
    "serviceCharge" numeric NOT NULL,
    "grantTotal" numeric NOT NULL,
    promocode character varying COLLATE pg_catalog."default",
    "promocodeAmount" numeric,
    "paymentType" character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "UserTransaction_pkey" PRIMARY KEY ("transactionId"),
    CONSTRAINT "bookingTransaction" FOREIGN KEY ("bookingId")
        REFERENCES dbo."UserBookings" ("bookingId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS dbo."UserBookingTransaction"
    OWNER to postgres;
-- Index: fki_bookingTransaction

-- DROP INDEX IF EXISTS dbo."fki_bookingTransaction";

CREATE INDEX IF NOT EXISTS "fki_bookingTransaction"
    ON dbo."UserBookingTransaction" USING btree
    ("bookingId" ASC NULLS LAST)
    TABLESPACE pg_default;
