/******************************************************************************
**  Name: GetUserDetailsById
**  Desc: Get User Details by userId
**
**  Author:    Bhushan Bapat
**
**  Date: 19/10/2022
*******************************************************************************
**                            Change History
*******************************************************************************
**   Date:     Author:                            Description:
** --------   --------         ---------------------------------------------------
** 19/10/2022 Bhushan Bapat  Created Stored Procedure to get User by ID

*******************************************************************************/
CREATE PROCEDURE dbo."GetUserDetailsById"(IN _UserID UUID)


LANGUAGE 'plpgsql'
AS $BODY$
BEGIN


  SELECT
    u.UserId,
    u.FirstName,
    u.LastName,
    u.MiddleName,
    u.UserName,
    u.DOB,
    u.MobileNo,
    u.CreatedBy,
    u.CreatedDate,
    u.UpdatedBy,
    u.UpdatedDate
    FROM dbo.User u
    where u.UserId=_UserId

END
$BODY$;
ALTER PROCEDURE dbo."GetUserDetailsById"()
OWNER TO postgres;
