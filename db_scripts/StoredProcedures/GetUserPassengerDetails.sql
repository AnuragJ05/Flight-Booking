/******************************************************************************
**  Name: GetUserPassengerDetails
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
CREATE PROCEDURE dbo."GetUserPassengerDetails"()
  IN _UserID UUID,

LANGUAGE 'plpgsql'
AS $BODY$
BEGIN

  SELECT
    p.passengerId,
	  p.FirstName,
    p.LastName,
    p.MiddleName,
    p.UserName,
	  p.DOB,
	  p.AdhaarNo,
	  p.PanCardNo
    FROM dbo.UserPassengerDetails p
    where p.UserId=_UserId

  END
  $BODY$;
  ALTER PROCEDURE dbo."GetUserPassengerDetails"()
      OWNER TO postgres;
