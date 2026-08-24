#1 requests library is used to send HTTP requests to APIs
import requests

#2
# This function calls the FreeAPI and retrieves random user data.
# We will extract username, country, and latitude from the API response.
def fetch_random_user_freeapi():

  # URL/endpoint of the API from where we want to get the data
  url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

  # Send a GET request to the API.
  # The API server processes our request and sends back a response.
  response = requests.get(url)

  # Convert the JSON response into a Python object.
  # Usually, the API returns JSON, which becomes a Python dictionary/list.
  data = response.json()


  #3
  # Check whether the API request was successful
  # AND whether the response contains the "data" key.
  #
  # data["success"] → checks API's success status
  # "data" in data → checks whether actual user data exists
  if data["success"] and "data" in data:

    #4
    # Extract the actual user information from the "data" key.
    # user_data is now a Python dictionary containing user details.
    user_data = data["data"]


    #5
    # Extract only the information we need from the user_data dictionary.
    #
    # Nested dictionary access:
    #
    # user_data
    #    ├── login
    #    │     └── username
    #    │
    #    └── location
    #          ├── country
    #          └── coordinates
    #                └── latitude

    username = user_data["login"]["username"]

    country = user_data["location"]["country"]

    latitude = user_data["location"]["coordinates"]["latitude"]


    #6
    # Return the extracted values to the function caller.
    #
    # Multiple values are returned as a tuple:
    # (username, country, latitude)
    return username, country, latitude


  else:
    #7
    # If the API response is not successful or required data is missing,
    # raise an exception.
    #
    # raise → stops normal execution and sends the error to the caller.
    raise Exception("Failed to fetch user data!")


#8
# main() is the main entry point of our program.
def main():

  #10
  # Use try-except to safely handle errors.
  # This prevents the program from crashing suddenly when an error occurs.
  try:

    #12
    # Call our API function and receive the returned values.
    #
    # The function returns:
    # (username, country, latitude)
    #
    # These values are unpacked into three variables.
    username, country, latitude = fetch_random_user_freeapi()

    # Display the extracted API data.
    print(
      f"Username: {username}, "
      f"\nCountry: {country}, "
      f"\nLatitude: {latitude}"
    )


  #11
  # Handle errors specifically related to the requests library.
  #
  # Examples:
  # - Internet connection problem
  # - Connection failure
  # - Request failure
  except requests.RequestException as e:
    print(f"Request error: {e}")


  # Handle any other unexpected error.
  #
  # For example:
  # - KeyError
  # - TypeError
  # - Exception raised by our own code
  except Exception as e:
    print(f"Error: {e}")


#9
# This condition checks whether this Python file is being
# executed directly rather than imported as a module.
#
# If we run:
# python free_api_username_country.py
#
# __name__ becomes "__main__", so main() will execute.
if __name__ == "__main__":
  main()



'''
The most important flow to remember:
API
 ↓
requests.get(url)
 ↓
HTTP Response
 ↓
response.json()
 ↓
Python Dictionary
 ↓
Check success
 ↓
Extract required data
 ↓
return username, country, latitude
 ↓
main()
 ↓
print()



And your error-handling flow:
API Request
     │
     ├── RequestException ──→ Network/API request error
     │
     ├── Other Exception ───→ KeyError / TypeError / etc.
     │
     └── Success ───────────→ Process JSON data
'''