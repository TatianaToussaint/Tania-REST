Feature: Airportgap.com REST API
  Description: Based on the airoport ticker, the API provides
  information about the airport geographical location

  Background: Given base uri 'https://airportgap.com/api'

    Scenario Outline: Submit GET request with an airport ticker
      Given Airport ticker is <ticker>
      When GET request is submitted to the end point  /airports/<ticker>
      Then country is <country>

      Examples:
        | ticker  | country |
        | KIX     | Japan   |
        | SFO     | United States |
        | FCO     | Italy         |

