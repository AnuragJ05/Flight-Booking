  /******************************************************************************
  **  Name: CreateUser
  **  Desc: Creates a new user and sets its initial password.
  **
  **  Author:    Bhushan Bapat
  **
  **  Date: 19/10/2022
  *******************************************************************************
  **                            Change History
  *******************************************************************************
  **   Date:     Author:                            Description:
  ** --------   --------         ---------------------------------------------------
  ** 19/10/2022 Bhushan Bapat  Created Stored Procedure to add User to the database
  ** 20/10/2022 Bhushan Bapat  Added AddPasswordPassword SP to this SP
  *******************************************************************************/
  CREATE PROCEDURE [dbo."CreateUser"()
    OUT _UserID UUID,
    IN _FirstName text,
    IN _LastName text,
    IN _MiddleName text,
    IN _UserName character varying ,
    IN _MobileNo numeric(10,0),
    IN _DOB DATE,
    IN _CreatedBy UUID,
    IN _CreatedDate DATE,
    IN _UpdatedBy UUID,
    IN _UpdatedDate DATE
    IN _passwordHash

  LANGUAGE 'plpgsql'
  AS $BODY$
  BEGIN

    DECLARE _UtcNow datetime

    SET _UtcNow = GetUtcDate()
    SET _UserId = NEWID()

    INSERT INTO dbo.User
    (
      Userid,
      FirstName,
      LastName,
      MiddleName,
      UserName,
      MobileNo,
  	  DOB,
  	  CreatedBy,
  	  CreatedDate,
  	  UpdatedBy,
  	  UpdatedDate
    )
    SELECT
      UserId			= _UserID,
  	  FirstName		= _FirstName,
      LastName		= _LastName,
      MiddleName      = _MiddleName,
      UserName        = UserName,
  	  DOB				= _DOB,
  	  MobileNo		= _MobileNo
  	  CreatedBy		= _CreatedBy
  	  CreatedDate		= _CreatedDate
  	  UpdatedBy		= _UpdatedBy
  	  UpdatedDate		= _UpdatedDate

  DECLARE _PasswordId uuid
  SET PasswordId = NEWID()
    EXEC dbo.AddUserPassword
      UserPasswordId = _PasswordId,
      UserId         = _UserId,
      PasswordHash   = _PasswordHash,
  	createdDate    = _CreatedDate

  END
  $BODY$;
ALTER PROCEDURE dbo."CreateUser"()
  OWNER TO postgres;
