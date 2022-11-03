/******************************************************************************
**  Name: AddUserPassenger
**  Desc: Add Passengers to Users
**
**  Author:    Bhushan Bapat
**
**  Date: 21/10/2022
*******************************************************************************
**                            Change History
*******************************************************************************
**   Date:     Author:                            Description:
** --------   --------         ---------------------------------------------------

*******************************************************************************/
CREATE PROCEDURE dbo."AddUserPassenger"()
  IN _UserID UUID,
  IN _FirstName text,
  IN _LastName text,
  IN _MiddleName text,
  IN _MobileNo numeric(10,0),
  IN _DOB DATE,
  IN _AdhaarNo numeric(12,0),
  IN _PanCardNo character varying (10),

LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
  SET NOCOUNT ON

  SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED

  DECLARE _PassengerId UUID

  SET _PassengerId = NEWID()

  INSERT INTO dbo.UserPassengerDetails
  (
    Userid,
	  PassengerId
    FirstName,
    LastName,
    MiddleName,
    MobileNo,
	  DOB,
	  AdhaarNo,
	  PanCardNo
  )
  SELECT
    UserId			 = _UserID,
	  PassengerId	 = _PassengerId,
	  FirstName		 = _FirstName,
    LastName		 = _LastName,
    MiddleName   = _MiddleName,
    UserName     = UserName,
	  DOB      		 = _DOB,
	  AdhaarNo		 = _AdhaarNo,
	  PanCardNo		 = _PanCardNo

  END
  $BODY$;
  ALTER PROCEDURE dbo."AddUserPassenger"()
      OWNER TO postgres;
