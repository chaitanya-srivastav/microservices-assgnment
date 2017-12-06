PART 3 : TAKE HOME ASSIGNMENT
DURATION: 24 - 72h (Negotiable)

/// PROBLEM BACKGROUND: ///

AirAsia CRM team would like to search for customers who will fly for the next 7 days based on CRM team searched customer's departure station.
Make a "GET" call to the following CRM API to obtain the data: https://us-central1-airasiawebanalytics.cloudfunctions.net/interviewAPIdata/nextflight
Every call to the API must be authenticated, which must be done by adding a custom HTTP header with username (airasia) and password (AllStars9).
The response of your API must in the format  >>>>>>>
<DepatureStationArrivalStation>: 
concatenate "NEXT_DEPARTURESTATION" and 
"NEXT_ARRIVALSTATION".
<CustomerID>: the "customerID"

/// SAMPLE OUTPUT FOR APPLICATION: ///

  "key_id": "3",
  "contacts":
  [
    {
      "2": <DepatureStationArrivalStation>,
      "source_id": <CustomerID>
    }
  ]
}

/// SUBMISSTION REQUIREMENTS: ///
1. Build a microservice in flask
2. Answer the problem with a RESTful API
3. API must be LIVE and DEPLOYED on Google App Engine
4. API must be BUILT on top of SAMPLE CODE provided (microservice folder)
5. API must have authentication
6. API must have instructions on how to call & sample payload the RESTful service on the index page ('/')
7. Include repo link for this project in the index page ('/')
8. Use of documentation frameworks (swagger/flassger) is encouraged
