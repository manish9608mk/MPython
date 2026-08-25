
#1
from pymongo import MongoClient
from bson import ObjectId

from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get MongoDB credentials from environment variables
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
cluster = os.getenv("MONGO_CLUSTER")

#2
# Connect to MongoDB
client = MongoClient(
    f"mongodb+srv://{username}:{password}@{cluster}/",
    tlsAllowInvalidCertificates=True
)
print(client)

#3
database = os.getenv("MONGO_DATABASE")
db = client[database]


#4
video_collection = db["videos"]
# print(video_collection)


#7
def list_videos():
    print("-" * 70)

    for video in video_collection.find():
        print(f"\nID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

    print("-" * 70)


#8
def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


#9
# Updating a video requires three parameters:
# 1. video_id      -> identifies which video should be updated
# 2. updated_name  -> the new name of the video
# 3. updated_time  -> the new time of the video
#
# update_one() first finds the document using its _id,
# then $set updates the specified fields with the new values.
def update_video(video_id, updated_name, updated_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {'$set': {'name': updated_name, 'time': updated_time}}
    )

#10
# Delete the video by finding it using its unique _id.
def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})


#5 
def main():
  #6
  while True:
    print("\nYoutube Manager App Using Mongodb")
    print("1. List all videos: ")
    print("2. Add new video: ")
    print("3. Update a video: ")
    print("4. Delete a video: ")
    print("5. Exit the app.")

    choice = int(input("Enter your choice: "))

    if choice == 1:
      list_videos() #7

    elif choice == 2:
      name = input("Enter video name: ")
      time = input("Enter video time: ")
      add_video(name, time) #8

    elif choice == 3:
       video_id = input("Enter video video ID to update: ")
       updated_name = input("Enter the updated video name: ")
       updated_time = input("Enter the updated video time: ")
       update_video(video_id, updated_name, updated_time) #9

    elif choice == 4:
      video_id = input("Enter the video id to delete: ")
      delete_video(video_id) #10
      
    elif choice == 5:
      break

    else:
      print("Invalid choice!")
      

 #5
if __name__ == "__main__":
  main()




'''
Flow Diagram:

.env
 │
 ├── username
 ├── password
 ├── cluster
 └── database
       ↓
load_dotenv()
       ↓
os.getenv(...)
       ↓
MongoClient(...)
       ↓
database
       ↓
videos collection
       ↓
CRUD operations
'''