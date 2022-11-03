/******************************************************************************
**  Name: AddBookingTransaction
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
** 23/10/2022 Bhushan Bapat  Created Stored Procedure to add Booking Transation
** 24/10/2022 Bhushan Bapat	 Added Stored Procedure for Individual Payment

*******************************************************************************/
CREATE PROCEDURE dbo."AddBookingTransaction"()
	IN	_BookingId	 Uuid ,
	IN	_TransactionId	 Uuid ,
	IN	_TotalAmount	 Numeric ,
	IN	_CGST	 Numeric ,
	IN	_SGST	 Numeric ,
	IN	_ServiceCharge	 Numeric ,
	IN	_GrantTotal	 Numeric ,
	IN	_Promocode 	Character Varying ,
	IN	_PromocodeAmount	 Numeric,
	IN	_PaymentType	 Character Varying

  LANGUAGE 'plpgsql'
  AS $BODY$
  BEGIN
	INSERT INTO dbo.UserBookingTransaction
	  (
		BookingId	,
		TransactionId	,
		TotalAmount	,
		CGST	,
		SGST	,
		ServiceCharge	,
		GrantTotal	,
		Promocode 	,
		PromocodeAmount	,
		PaymentType
	)
	SELECT
		BookingId	=	_BookingId
		TransactionId	=	_TransactionId
		TotalAmount	=	_TotalAmount
		CGST	=	_CGST
		SGST	=	_SGST
		ServiceCharge	=	_ServiceCharge
		GrantTotal	=	_GrantTotal
		Promocode 	=	_Promocode
		PromocodeAmount	=	_PromocodeAmount
		PaymentType	=	_PaymentType

    DECLARE _IndividualPaymentId uuid
    SET _IndividualPaymentId= NEWID()
    EXEC dbo.SetIndividualFlightPayemnt
      IndividualPaymentId	=	_IndividualPaymentId
      Transactionid	=	_Transactionid
      FlightId	=	_FlightId
      BaseFare	=	_BaseFare
      ConvenienceFees	=	_ConvenienceFees

  END
  $BODY$;
ALTER PROCEDURE dbo."AddBookingTransaction"()
  OWNER TO postgres;
