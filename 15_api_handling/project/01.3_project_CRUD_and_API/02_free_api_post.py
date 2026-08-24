#1 requests library is used to send HTTP requests to APIs
import requests


#2 method for retrieving data like username, country, latitude, city etc.
def fetch_random_user_freeapi():
  url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

  # Send GET request with a 10-second timeout
  response = requests.get(url, timeout=10)

  # Raise an exception if the server returns an HTTP error
  # such as 400, 404, 500, etc.
  response.raise_for_status()

  data = response.json()

  #3
  if data["success"] and "data" in data:
    #4
    user_data = data["data"]

    #5
    username = user_data["login"]["username"]
    country = user_data["location"]["country"]
    latitude = user_data["location"]["coordinates"]["latitude"]

    #6
    return username, country, latitude

  else:
    #7 raise: raise an error if data is not found
    raise Exception("Failed to fetch user data!")


#13
# This function sends new data to the server using a POST request.
def create_post():

  # API endpoint where we want to send/create new data
  url = "https://jsonplaceholder.typicode.com/posts"

  # Data that we want to send to the server.
  # This Python dictionary will be converted into JSON.
  payload = {
    "title": "Learning API",
    "body": "Learning POST request with Python",
    "userId": 1
  }

  #14
  # Send POST request to the API.
  # json=payload automatically converts the Python dictionary
  # into JSON and sends it in the request body.
  response = requests.post(
    url,
    json=payload,
    timeout=10
  )

  #15
  # Raise an exception if the server returns an HTTP error
  # such as 400, 404, 500, etc.
  response.raise_for_status()

  #16
  # Convert the JSON response from the server
  # into a Python dictionary.
  data = response.json()

  #17
  # Return the response data to the function caller.
  return data


#8
def main():

  #10 To protect main() from crashing - use try-except
  try:

    #12 calling GET method
    username, country, latitude = fetch_random_user_freeapi()

    print(
      f"Username: {username}, "
      f"\nCountry: {country}, "
      f"\nLatitude: {latitude}"
    )


    #18
    # Call the POST function to create/send new data.
    created_post = create_post()

    #19
    # Display the response received from the server.
    print("\nPOST Response:")
    print(created_post)


  #11
  except requests.RequestException as e:
    print(f"Request error: {e}")

  except Exception as e:
    print(f"Error: {e}")


#9
if __name__ == "__main__":
  main()