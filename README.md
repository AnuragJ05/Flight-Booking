# Flight-Booking

The Flight Ticketing System project will serve a travel organization to host its flight ticket booking and management system online. This provides an efficient way to interact with customers in a seamless and automated manner as well as processing ticket booking online from the organization's perspective as well.  

This would help streamline the ticketing process in three ways-

1) There would be a single place where customers can interact and better manage their booking needs through the automated process.  
2) This would be a big boost for the travel organization towards technology which will further improve their ticket management and reduce manual employee overhead for tasks that can be automated which saves both time and critical resources. 
3) Would facilitate data analytics to prepare the organization to meet customer told & untold needs. 

## APIs

### 1)  Register User
    Post : http://localhost:5050/register
``` 
    response: 
    
    {
            "username": "dummy",
            "password": "12345678",
            "firstName": "dummy",
            "middleName": "dummy",
            "lastName": "dummy",
            "DOB": "05/11/1998",
            "mobileNo": "0999679302"
    }

```

### 2)  User Login

    Post : http://localhost:5050/login
``` 
    response: 

        {
                "username": "dummy",
                "password": "12345678"
        }

```


### 3)  Flight Details 

    This feature will let customers view options to choose from and filter based on below: 

    Source/Destination 
    Airline 
    Type of flight
    Date and Time 
    Packages 

    Get : http://localhost:5050/flight
``` 
    response: 

    [
        {
            "PNR": "171515",
            "airlineVendor": "US Airlines",
            "arrivalTime": "2022-11-16T06:30",
            "baseFare": 8000,
            "departureTime": "2022-11-16T21:30",
            "duration": 590,
            "flightNo": "192837262",
            "flightType": "Charter",
            "from": "GRU",
            "journeyType": "One-way",
            "to": "JFK",
            "travelClass": "First Class",
            "travelDate": "2022-11-10"
        }
    ] 

```
### 4) Register Passenger Details

    Post : http://localhost:5050/passenger
``` 
    request: 

    {
        "firstName": "test2",
        "middleName": "test2",
        "lastName": "test2",
        "DOB": "05/11/2000",
        "mobileNo": "0999675302",
        "adhaarNo": 234582829191,
        "panCardNo" : "BI97B7V"
    }

    response: 

    {
        "message": "passenger created successful!!"
    }
```


### 5) Get Passenger details 

    Get : http://localhost:5050/passenger
``` 
    response: 

    [
        {
            "DOB": "Thu, 10 Oct 1991 00:00:00 GMT",
            "adhaarNo": "121282829191",
            "firstName": "A",
            "lastName": "C",
            "middleName": "B",
            "mobileNo": "7799887765",
            "panCardNo": null,
            "passengerId": "cf093eed-27e9-46aa-a9c3-518dbc5892a3",
            "userid": "a55b99a8-8182-459e-8b67-78abc73d5a06"
        }
    ]
```


### 6) Tickets Booking

    This feature will let customers book or cancel flight tickets as per their requirements. 

    post: http://localhost:5050/book
```
    request:
 
    {
        "flight": {
            "PNR": "171515",
            "flightNo": "192837262",
            "flightType": "Charter",
            "airlineVendor": "US Airlines",
            "journeyType": "One-way",
            "travelClass": "First Class",
            "duration": 590,
            "travelDate": "2022-11-16",
            "departureTime": "2022-11-16T21:30",
            "arrivalTime": "2022-11-16T06:30",
            "from": "GRU",
            "to": "JFK",
            "baseFare": 8000
        },
        "passenger": [
            {
                "passengerId" : "cf093eed-27e9-46aa-a9c3-518dbc5892a3",
                "seatNo" : "34B"
            }
        ],
        "payment" : {
            "totalAmount" : 8000,
            "CGST": 750,
            "SGST": 750,
            "serviceCharge" : 1000,
            "grantTotal" : 10500,
            "promocode" : "NA",
            "promocodeAmount" : 0,
            "paymentType": "CASH"
            }
        }

    response:

    {
        "message": "booking successful!!"
    }
```

