# Import the necessary modules
import requests

# Define a function to convert currencies
def currency_converter(amount, from_currency, to_currency):
    # Set the API endpoint for currency conversion
    api_endpoint = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    
    # Send a GET request to the API endpoint
    response = requests.get(api_endpoint)
    
    # Get the JSON data from the response
    data = response.json()
    
    # Extract the exchange rate for the target currency
    exchange_rate = data["rates"][to_currency]
    
    # Calculate the converted amount
    converted_amount = amount * exchange_rate
    
    # Return the converted amount
    return converted_amount

# Prompt the user to enter the amount, source currency, and target currency
amount = float(input("Enter the amount: "))
from_currency = input("Enter the source currency code: ").upper()
to_currency = input("Enter the target currency code: ").upper()

# Convert the currency and print the result
result = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")


'''
Explanation:

In this code, we define a function called currency_converter() that takes an amount, source currency code, and target currency code as arguments and returns the converted amount.
We first set the API endpoint for currency conversion using the from_currency parameter and the requests module to send a GET request to the endpoint.
We then extract the exchange rate for the target currency from the JSON data returned by the API using the to_currency parameter and calculate the converted amount by multiplying the exchange rate with the amount parameter.
Finally, we prompt the user to enter the amount, from_currency, and to_currency using the input() function and pass them to the currency_converter() function to convert the currency. The converted amount is then printed using string formatting.
'''