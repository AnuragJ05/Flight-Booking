/******************************************************************************
**  Name: AddBookingItenraray
**  Desc: Add  Booking Intenrary
**
**  Author:    Bhushan Bapat
**
**  Date: 24/10/2022
*******************************************************************************
**                            Change History
*******************************************************************************
**   Date:     Author:                            Description:
** --------   --------         ---------------------------------------------------
** 24/10/2022 Bhushan Bapat  Created Stored Procedure to add Booking Itenrary for the user

*******************************************************************************/
CREATE PROCEDURE dbo."AddBookingItenraray"(
	IN _ItenraryId uuid,
	IN _BookingId uuid ,
	IN _PNR character varying,
	IN _From character varying,
	IN _To character varying,
	IN _TravelDate date ,
	IN _DepartureTime date ,
	IN _ArrivalTime date ,
	IN _JourneyType character varying,
	IN _TravelClass character varying,
	IN _AirlineVendor character varying,
	IN _FlightNo character varying,
	IN _FlightType character varying,
	IN _BaseFare numeric)

  LANGUAGE 'plpgsql'
  AS $BODY$
  BEGIN
  	INSERT INTO dbo.BookingItenrary
  	  (
  		Itenraryid	,
  		Bookingid	,
  		Pnr	,
  		From	,
  		To	,
  		Traveldate	,
  		Departuretime	,
  		Arrivaltime	,
  		Journeytype	,
  		Travel	,
  		Airlinevendor	,
  		Flightno	,
  		Flighttype	,
  		Basefare
  	)
  	SELECT
  		Itenraryid	=	_Itenraryid	,
  		Bookingid	=	_Bookingid	,
  		Pnr	=	_Pnr	,
  		From	=	_From	,
  		To	=	_To	,
  		Traveldate	=	_Traveldate	,
  		Departuretime	=	_Departuretime	,
  		Arrivaltime	=	_Arrivaltime	,
  		Journeytype	=	_Journeytype	,
  		Travel	=	_Travel	,
  		Airlinevendor	=	_Airlinevendor	,
  		Flightno	=	_Flightno	,
  		Flighttype	=	_Flighttype	,
  		Basefare	=	_Basefare

  END
$BODY$;
ALTER PROCEDURE dbo."AddBookingItenraray"()
    OWNER TO postgres;
