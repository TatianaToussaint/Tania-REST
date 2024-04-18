Feature: Zippopotam REST API
  Description: API provides geographical information about the place
  based on its postal zip code or city name

  Background:
    Given base uri is 'http://api.zippopotam.us'

    @zipcode
    Scenario: Submit a GET request with a country zip code
      Given zip code is 94404
      When GET request is submitted to the endpoint '/us/94404'
      Then response status code is 200
      And response 'Content_type' header is 'application/json'
      And 'place name' is 'San Moteo'
      And 'state' is 'California'

    Scenario: Submit a GET request with a city name
      Given city is 'San Mateo'
      When GET request is submitted to the endpoint '/us/ca/San Mateo'
      Then 'places' list has 9 objects
