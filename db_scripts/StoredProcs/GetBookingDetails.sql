/******************************************************************************
**  Name: GetBookingDetails
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
** 23/10/2022 Bhushan Bapat	 Added Stored Procedure for getting Booking Details

*******************************************************************************/
CREATE PROCEDURE dbo."GetBookingDetails"(
	IN _BookingId UUID,
  IN _UserId UUID)

  LANGUAGE 'plpgsql'
  AS $BODY$
  BEGIN

    SELECT
        b.UserId,
  	    b.BookingId,
  	    b.BookingDate,
        b.BookingStatus,
      	i.Itenraryid,
      	i.Pnr,
      	i.From,
      	i.To,
      	i.Traveldate,
      	i.Departuretime,
      	i.Arrivaltime,
      	i.Journeytype,
      	i.Travel,
      	i.Airlinevendor,
      	i.Flightno,
      	i.Flighttype,
      	i.Basefare,
      	i.Basefare,
      	bp.Id,
      	bp.PassengerId,
        p.FirstName,
        p.MiddleName,
        p.LastName,
      	bp.SeatNo,
        bt.Transactionid,
        bt.Totalamount,
        bt.CGST,
        bt.SGST,
        bt.ServiceCharge,
        bt.GrantTotal,
        bt.Promocode,
        bt.PromocodeAmount,
        bt.PaymentType

          FROM dbo.UserBookings b
          INNER JOIN dbo.BookingItenraray i on b.bookingId=i.bookingId
          INNER JOIN dbo.UserBookingTransaction bt on bt.bookingId = b.bookingId
          INNER JOIN dbo.UserBookingPassenger bp on bp.bookingId = b.bookingId
          INNER JOIN dbo.UserPassengerDetails p on p.passengerId=bp.passengerId
          where b.userId = _UserId and b.bookingId=_BookingId


  END
  $BODY$;
ALTER PROCEDURE dbo."GetBookingDetails"()
    OWNER TO postgres;
