#1 requests library is used to send HTTP requests to APIs
import requests

#2 method for retrieving data like username, country, latitude, city etc.
def fetch_random_user_freeapi():
  url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
  response = requests.get(url)
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

#8
def main():
  #10 To protect main() or crashing main() - user try-except
  try:
    #12 calling methods 
    username, country, latitude = fetch_random_user_freeapi()

    print(f"Username: {username}, \nCountry: {country}, \nLatitude: {latitude}")

  #11
  except requests.RequestException as e:
    print(f"Request error: {e}")

  except Exception as e:
   print(f"Error: {e}")

#9
if __name__ == "__main__":
  main()


