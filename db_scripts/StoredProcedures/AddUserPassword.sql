/******************************************************************************
**  Name: AddUserPassword
**  Desc: Add Password to a new user
**
**  Author:    Bhushan Bapat
**
**  Date: 20/10/2022
*******************************************************************************
**                            Change History
*******************************************************************************
**   Date:     Author:                            Description:
** --------   --------         ---------------------------------------------------

*******************************************************************************/
CREATE PROCEDURE dbo."AddUserPassword"()
   IN _PasswordId uuid,
   IN _UserId uuid,
   IN _PasswordHash character varying,
   IN createdDate    = _CreatedDate

   LANGUAGE 'plpgsql'
   AS $BODY$
   BEGIN

    INSERT INTO dbo.UserPasswordEntity
    (
      UserPasswordId,
      UserId,
      PasswordHash,
      CreatedDate,
    )
    SELECT
      UserPasswordId	= _PasswordId,
  	  UserId			= _UserID,
  	  CreatedDate		= _CreatedDate,

  END
$BODY$;
ALTER PROCEDURE dbo."AddUserPassword"()
    OWNER TO postgres;
