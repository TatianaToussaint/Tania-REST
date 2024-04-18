Feature: Verify user information retrieval
  Description: API client to retrieve user information and can verify details about the users

  Background:
    Given base uri is 'https://reqres.in/api'

  Scenario: Retrieve user with ID 8 and verify last name and URL in the response
    Given endpoint '/users/8'
    When send a GET request to the endpoint
    Then response status code is 200
    And The response to contain JSON
    And The JSON response should have 'last_name' with value 'Ferguson'
    And The JSON response should have 'url' with value 'https://reqres.in/#support-heading'