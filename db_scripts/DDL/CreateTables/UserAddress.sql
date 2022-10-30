-- Table: dbo.Payment

-- DROP TABLE IF EXISTS dbo."Payment";

CREATE TABLE IF NOT EXISTS dbo."Payment"
(
    "transactionId" uuid NOT NULL,
    "flightId" uuid NOT NULL,
    "individualPaymentId" uuid NOT NULL,
    "baseFare" numeric NOT NULL,
    "convenienceFee" numeric NOT NULL,
    CONSTRAINT "Payment_pkey" PRIMARY KEY ("individualPaymentId"),
    CONSTRAINT "ItenraryPayment" FOREIGN KEY ("flightId")
        REFERENCES dbo."BookingItenrary" ("itenraryId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT transaction FOREIGN KEY ("transactionId")
        REFERENCES dbo."UserBookingTransaction" ("transactionId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS dbo."Payment"
    OWNER to postgres;
-- Index: fki_ItenraryPayment

-- DROP INDEX IF EXISTS dbo."fki_ItenraryPayment";

CREATE INDEX IF NOT EXISTS "fki_ItenraryPayment"
    ON dbo."Payment" USING btree
    ("flightId" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: fki_transaction

-- DROP INDEX IF EXISTS dbo.fki_transaction;

CREATE INDEX IF NOT EXISTS fki_transaction
    ON dbo."Payment" USING btree
    ("transactionId" ASC NULLS LAST)
    TABLESPACE pg_default;
