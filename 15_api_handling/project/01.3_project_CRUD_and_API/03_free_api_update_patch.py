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



#20
# This function updates an existing post using a PATCH request.
def update_post():

  # API endpoint of the post we want to update.
  # /1 means we want to update post with ID 1.
  url = "https://jsonplaceholder.typicode.com/posts/1"

  #21
  # Data containing only the fields we want to update.
  #
  # PATCH updates only the provided fields
  # instead of replacing the complete resource.
  payload = {
    "title": "Updated API Learning"
  }

  #22
  # Send PATCH request to update the existing post.
  # json=payload sends our updated data as JSON.
  response = requests.patch(
    url,
    json=payload,
    timeout=10
  )

  #23
  # Raise an exception if the server returns an HTTP error.
  response.raise_for_status()

  #24
  # Convert the server's JSON response
  # into a Python dictionary.
  data = response.json()

  #25
  # Return the updated post data.
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


    #26
    # Call the PATCH function to update existing data.
    updated_post = update_post()

    #27
    # Display the updated data received from the server.
    print("\nPATCH Response:")
    print(updated_post)


  #11
  except requests.RequestException as e:
    print(f"Request error: {e}")

  except Exception as e:
    print(f"Error: {e}")


#9
if __name__ == "__main__":
  main()



'''
The most important difference:

requests.post(url, json=payload)
means:
Create/send new data

while,

requests.patch(url, json=payload)
means:
Update specific fields of existing data


Before
────────────────────────
ID      1
Title   Learning API
Body    Learning POST...
UserID  1


PATCH
{
    "title": "Updated API Learning"
}


After
────────────────────────
ID      1
Title   Updated API Learning  ← changed
Body    Learning POST...      ← unchanged
UserID  1                     ← unchanged




UPDATE operation:

For API CRUD, update can be done mainly using:

PUT → replace the complete resource
PATCH → update only specific fields

For now, learn PATCH first because it is easier and very commonly used when only some fields need changing.



'''