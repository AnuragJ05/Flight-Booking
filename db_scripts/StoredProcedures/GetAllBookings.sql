/******************************************************************************
**  Name: GetAllBookings
**  Desc: To get the booking details for a User and bookingId
**
**  Author:    Bhushan Bapat
**
**  Date: 23/10/2022
*******************************************************************************
**                            Change History
*******************************************************************************
**   Date:     Author:                            Description:
** --------   --------         ---------------------------------------------------
** 24/10/2022 Bhushan Bapat	 Added Stored Procedure for Booking Itenrary

*******************************************************************************/
CREATE PROCEDURE dbo."GetAllBookings"(IN _UserId UUID)

  LANGUAGE 'plpgsql'
  AS $BODY$
  BEGIN

    SELECT
      b.UserId,
  	  b.BookingId,
  	  b.BookingDate,
      b.BookingStatus,
      i.Itenraryid,
      i.Bookingid,
      i.Pnr,
      i.From,
      i.To,
      i.Traveldate,
      i.Departuretime,
      i.Arrivaltime,


          FROM dbo.UserBookings b
          INNER JOIN dbo.BookingItenraray i on b.bookingId=i.bookingId
          where b.userId = _UserId


  END
  $BODY$;
ALTER PROCEDURE dbo."GetAllBookings"()
    OWNER TO postgres;
