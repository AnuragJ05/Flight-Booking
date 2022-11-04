/******************************************************************************
**  Name: CreateUserBooking
**  Desc: Add New Booking for a User
**
**  Author:    Bhushan Bapat
**
**  Date: 23/10/2022
*******************************************************************************
**                            Change History
*******************************************************************************
**   Date:     Author:                            Description:
** --------   --------         ---------------------------------------------------
** 23/10/2022 Bhushan Bapat  Created Stored Procedure to add Booking for the user
** 24/10/2022 Bhushan Bapat	 Added Stored Procedure for Booking Itenrary
** 24/10/2022 Bhushan Bapat Added Booking Passesnger Stored Procedure Call

*******************************************************************************/
CREATE PROCEDURE dbo."CreateUserBooking"(
	IN _UserID UUID,
	OUT _BookingId UUID,
	IN _BookingStatus character varying
  IN _PNR character varying
	IN _From character varying
	IN _To character varying
	IN _TravelDate date NOT NULL,
	IN _DepartureTime date NOT NULL,
	IN _ArrivalTime date NOT NULL,
	IN _JourneyType character varying
	IN _Travel
	IN _AirlineVendor character varying
	IN _FlightNo character varying
	IN _FlightType character varying
	IN _BaseFare numeric NOT NULL,
	IN _PassengerId uuid,
	IN _SeatNo character varying)

  LANGUAGE 'plpgsql'
  AS $BODY$
  BEGIN

    DECLARE _BookingId UUID
    DECLARE UtcNow datetime,

    SET _BookingId = NEWID()
    SET _UtcNow =  GetUtcDate()


    INSERT INTO dbo.UserBookings
    (
      BookingId,
  	  UserId
      BookingDate,
      BookingStatus,

    )
    SELECT
      UserId			= _UserID,
  	  BookingId		= _BookingId,
  	  BookingDate		= _UtcNow,
      BookingStatus	= _BookingStatus

    DECLARE _ItenraryId uuid
    SET _ItenraryId = NEWID()
    EXEC dbo.AddBookingItenraray(
      	_Itenraryid,
      	_Bookingid,
      	_Pnr,
      	_From,
      	_To,
      	_Traveldate,
      	_Departuretime,
      	_Arrivaltime,
      	_Journeytype,
      	_Travel,
      	_Airlinevendor,
      	_Flightno,
      	_Flighttype,
      	_Basefare,
      	_Basefare)

      DECLARE _Id uuid
      SET _Id = NEWID()
    	EXEC dbo.AddBookingPassenger(
      	_Id,
      	_BookingId,
      	_PassengerId,
      	_SeatNo)


        DECLARE _transactionId uuid
        SET _transactionId = NEWID()
      	EXEC dbo.AddBookingTransaction(
        	_Bookingid,
        	_Transactionid,
        	_Totalamount,
        	_CGST,
        	_SGST,
        	_ServiceCharge,
        	_Granttotal,
        	_Promocode,
        	_PromocodeAmount,
        	_PaymentType)

  END
  $BODY$;
ALTER PROCEDURE dbo."CreateUserBooking"()
    OWNER TO postgres;
