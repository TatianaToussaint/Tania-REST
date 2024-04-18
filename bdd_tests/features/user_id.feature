Feature: Verify user creation via API
  As an API client
  I want to verify that creating a new user returns a valid ID and timestamp
  So that I can ensure users are properly added to the system

  Background:
    Given the API base URL is "https://reqres.in/api"

  Scenario: Verifying a user creation returns a non-null ID and correct timestamp
    Given I set the API endpoint to "/users"
    And I set the request body to a user with name "Vlad" and job "Instructor"
    When I send a POST request to the endpoint
    Then the response should include a non-null "id"
    And the "createdAt" field should begin with "2023-03-"

