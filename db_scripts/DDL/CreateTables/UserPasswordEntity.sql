-- Table: dbo.UserPasswordEntity

-- DROP TABLE IF EXISTS dbo."UserPasswordEntity";

CREATE TABLE IF NOT EXISTS dbo."UserPasswordEntity"
(
    "userPasswordId" uuid NOT NULL,
    "userId" uuid NOT NULL,
    "passwordHash" character varying COLLATE pg_catalog."default" NOT NULL,
    "otpSecret" character varying COLLATE pg_catalog."default",
    "createdDate" date NOT NULL,
    CONSTRAINT "userPasswordEntity_pkey" PRIMARY KEY ("userPasswordId"),
    CONSTRAINT "userPassword" FOREIGN KEY ("userId")
        REFERENCES dbo."User" ("userId") MATCH SIMPLE
        ON UPDATE RESTRICT
        ON DELETE RESTRICT
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS dbo."UserPasswordEntity"
    OWNER to postgres;
-- Index: fki_userPassword

-- DROP INDEX IF EXISTS dbo."fki_userPassword";

CREATE INDEX IF NOT EXISTS "fki_userPassword"
    ON dbo."UserPasswordEntity" USING btree
    ("userId" ASC NULLS LAST)
    TABLESPACE pg_default;
