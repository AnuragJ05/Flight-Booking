/******************************************************************************
**  Name: GetUserDetailsByUserName
**  Desc: Get User Details by username
**
**  Author:    Bhushan Bapat
**
**  Date: 19/10/2022
*******************************************************************************
**                            Change History
*******************************************************************************
**   Date:     Author:                            Description:
** --------   --------         ---------------------------------------------------
** 19/10/2022 Bhushan Bapat  Created Stored Procedure to get User by username

*******************************************************************************/
CREATE PROCEDURE dbo."GetUserDetailsByUsername"(IN _Username character varying)


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
    where u.username= _Username

END
$BODY$;
ALTER PROCEDURE dbo."GetUserDetailsByUsername"()
OWNER TO postgres;
