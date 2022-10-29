# Flight-Booking

#APIs

1) Get : http://localhost:5050/flight

response: 
``` 
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

2) Get : http://localhost:5050/passenger

response: 
``` 
[
    [
        "cf093eed-27e9-46aa-a9c3-518dbc5892a3",
        "a55b99a8-8182-459e-8b67-78abc73d5a06",
        "A",
        "B",
        "C",
        "Thu, 10 Oct 1991 00:00:00 GMT",
        "7799887765",
        "121282829191",
        null
    ]
]
```

3) Post : http://localhost:5050/passenger

request: 
``` 
{
    "firstName": "test2",
    "middleName": "test2",
    "lastName": "test2",
    "DOB": "05/11/2000",
    "mobileNo": "0999675302",
    "adhaarNo": 234582829191,
    "panCardNo" : "BI97B7V"
}
```
response: 
``` 
{
    "message": "passenger created successful!!"
}
```

4) post: http://localhost:5050/book

request: 
``` 
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
```
response: 
``` 
{
    "message": "booking successful!!"
}
```

