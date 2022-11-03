/******************************************************************************
**  Name: AddBookingPassenger
**  Desc: Add Booking Passenger to the Booking
**
**  Author:    Bhushan Bapat
**
**  Date: 24/10/2022
*******************************************************************************
**                            Change History
*******************************************************************************
**   Date:     Author:                            Description:
** --------   --------         ---------------------------------------------------
** 24/10/2022 Bhushan Bapat  Created Stored Procedure to add Booking Passenger

*******************************************************************************/
CREATE PROCEDURE dbo."AddBookingPassenger"()
	IN _ID UUID,
	IN _BookingId UUID,
	IN _PassengerId uuid,
	IN _SeatNo character varying
  LANGUAGE 'plpgsql'
  AS $BODY$
  BEGIN
  	INSERT INTO dbo.BookingItenrary
  	  (
  		Id	,
  		Bookingid	,
  		PassengerId,
  		SeatNo
  	)
  	SELECT
  		Id			=	_Itenraryid	,
  		Bookingid	=	_Bookingid	,
  		PassengerId	=	_PassengerId
  		SeatNo		=	_SeatNo

  END
  $BODY$;
ALTER PROCEDURE dbo."AddBookingPassenger"()
  OWNER TO postgres;
