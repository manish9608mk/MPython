#1 requests library is used to send HTTP requests to APIs
import requests

# os is used to access environment variables.
import os


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



#28
# This function deletes an existing post from the server
# using a DELETE request.
def delete_post():

  # API endpoint of the post we want to delete.
  # /1 means we want to delete post with ID 1.
  url = "https://jsonplaceholder.typicode.com/posts/1"

  #29
  # Send DELETE request to the API.
  # The server will try to remove the resource with ID 1.
  response = requests.delete(
    url,
    timeout=10
  )

  #30
  # Raise an exception if the server returns an HTTP error
  # such as 400, 404, 500, etc.
  response.raise_for_status()

  #31
  # Return the HTTP status code received from the server.
  # 200 usually means the request was successful.
  return response.status_code



#34
# This function replaces an existing post using a PUT request.
def replace_post():

  # API endpoint of the post we want to replace.
  # /1 means we want to replace post with ID 1.
  url = "https://jsonplaceholder.typicode.com/posts/1"

  #35
  # Data that will replace the existing post.
  #
  # PUT generally replaces the complete resource
  # with the new data we provide.
  payload = {
    "id": 1,
    "title": "Learning PUT Request",
    "body": "Replacing complete post using Python",
    "userId": 1
  }

  #36
  # Send PUT request to replace the existing post.
  # json=payload sends our Python dictionary as JSON.
  response = requests.put(
    url,
    json=payload,
    timeout=10
  )

  #37
  # Raise an exception if the server returns an HTTP error
  # such as 400, 404, 500, etc.
  response.raise_for_status()

  #38
  # Convert the JSON response from the server
  # into a Python dictionary.
  data = response.json()

  #39
  # Return the replaced post data.
  return data



#42
# This function demonstrates how to send HTTP headers
# with an API request.
def fetch_post_with_headers():

  # API endpoint from where we want to retrieve a post.
  url = "https://jsonplaceholder.typicode.com/posts/1"

  #43
  # Headers contain additional information/metadata
  # that we want to send along with the HTTP request.
  #
  # Accept → tells the server what response format we prefer.
  # User-Agent → identifies the client making the request.
  headers = {
    "Accept": "application/json",
    "User-Agent": "Python-Requests"
  }

  #44
  # Send GET request with our custom headers.
  # headers=headers sends the headers to the server.
  response = requests.get(
    url,
    headers=headers,
    timeout=10
  )

  #45
  # Raise an exception if the server returns an HTTP error.
  response.raise_for_status()

  #46
  # Convert the JSON response into a Python dictionary.
  data = response.json()

  #47
  # Return the API response to the function caller.
  return data



#50
# This function demonstrates how to send query parameters
# with an API request.
def fetch_posts_with_params():

  # API endpoint from where we want to retrieve posts.
  url = "https://jsonplaceholder.typicode.com/posts"

  # Query parameters used to filter the API response.
  #
  # userId=1 means:
  # Return only posts belonging to user ID 1.
  params = {
    "userId": 1
  }

  #51
  # Send GET request with query parameters.
  # params=params automatically creates:
  # ?userId=1
  response = requests.get(
    url,
    params=params,
    timeout=10
  )

  #52
  # Raise an exception if the server returns an HTTP error.
  response.raise_for_status()

  #53
  # Convert the JSON response into a Python object.
  data = response.json()

  #54
  # Return the filtered posts.
  return data



#57
# This function demonstrates how to send an authentication token
# with an API request.
def fetch_post_with_auth():

  # API endpoint from where we want to retrieve a post.
  url = "https://jsonplaceholder.typicode.com/posts/1"

  #58
  # Read the authentication token from an environment variable.
  #
  # This is safer than hard-coding the token directly in the code.
  token = os.getenv("API_TOKEN")

  #59
  # Check whether the token exists.
  if not token:
    raise Exception("API_TOKEN environment variable is not set!")

  #60
  # Headers containing the authentication information.
  #
  # Authorization header sends the token to the server.
  headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json"
  }

  #61
  # Send GET request with authentication headers.
  response = requests.get(
    url,
    headers=headers,
    timeout=10
  )

  #62
  # Raise an exception if the server returns an HTTP error.
  response.raise_for_status()

  #63
  # Convert the JSON response into a Python object.
  data = response.json()

  #64
  # Return the API response.
  return data




#67
# This function demonstrates how to check the HTTP status code
# returned by the server after sending an API request.
def check_status_code():

    #68
    # API endpoint from where we want to retrieve a post.
    url = "https://jsonplaceholder.typicode.com/posts/1"

    #69
    # Send a GET request to the server.
    #
    # timeout=10 means:
    # Wait maximum 10 seconds for the server response.
    response = requests.get(
        url,
        timeout=10
    )

    #70
    # Print the HTTP status code returned by the server.
    #
    # Common HTTP status codes:
    # 200 → Request was successful
    # 201 → Resource was created
    # 400 → Bad request
    # 401 → Unauthorized
    # 403 → Forbidden
    # 404 → Resource was not found
    # 500 → Server error
    print("\nStatus Code:", response.status_code)

    #71
    # Check whether the server returned HTTP 200.
    #
    # HTTP 200 means:
    # The request was successfully processed by the server.
    if response.status_code == 200:

      #72
      # Execute this block when the status code is 200.
      print("Request successful!")

    else:

      #73
      # Execute this block when the status code
      # is anything other than 200.
      print("Request failed!")




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


    #32
    # Call the DELETE function to delete an existing post.
    delete_status = delete_post()

    #33
    # Display the status code received after deletion.
    print("\nDELETE Response:")
    print(f"Status Code: {delete_status}")


    #40
    # Call the PUT function to replace an existing post.
    replaced_post = replace_post()

    #41
    # Display the response received after replacing the post.
    print("\nPUT Response:")
    print(replaced_post)


    #48
    # Call the function that sends headers with a GET request.
    header_response = fetch_post_with_headers()

    #49
    # Display the response received from the API.
    print("\nHeaders Response:")
    print(header_response)

    #55
    # Call the function with query parameters.
    posts = fetch_posts_with_params()

    #56
    # Display the filtered posts.
    print("\nQuery Parameters Response:")
    print(posts)

    #65
    # Call the function that sends an authentication token.
    auth_response = fetch_post_with_auth()

    #66
    # Display the response received from the API.
    print("\nAuthentication Response:")
    print(auth_response)

    #74
    # Call the function that checks the HTTP status code.
    check_status_code()


  #11
  except requests.RequestException as e:
    print(f"Request error: {e}")

  except Exception as e:
    print(f"Error: {e}")


#9
if __name__ == "__main__":
  main()






'''
1. Terminal
   ↓
export API_TOKEN="test_token_123"

2. OS environment
   ↓
API_TOKEN

3. Python
   ↓
token = os.getenv("API_TOKEN")

4. Header
   ↓
Authorization: Bearer test_token_123

5. requests.get()
   ↓
API
   ↓
Response

'''