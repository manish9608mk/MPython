
import sqlite3

#1 Connect to database
conn = sqlite3.connect("youtube_video_sqlite3.db")

#2 Create cursor
cursor = conn.cursor()

#3 Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
""")

#4 Save table creation
conn.commit()


#9 List videos
def list_videos():
    print("-" * 50)

    cursor.execute("SELECT * FROM videos")

    videos = cursor.fetchall()

    if not videos:
        print("\nEmpty videos!")
        return

    for row in videos:
        print(row)

    print("-" * 50)


#10 Add video
def add_videos(name, time):
  cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)",(name, time))
  conn.commit()

#11 Update video
def update_video(video_id, new_name, new_time):
  cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
  conn.commit()


#12 Delete video
def delete_video(video_id):
  cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
  conn.commit()


#5 Main function
def main():

  #7 Menu loop
  while True:

    print("\nYoutube Manager App with SQLite3")

    print("1. List all youtube videos.")
    print("2. Add a youtube video.")
    print("3. Update a youtube video.")
    print("4. Delete a youtube video.")
    print("5. Exit the app.\n")

    choice = int(input("Enter your choice: "))

    #8 User choice
    if choice == 1:
     list_videos() #9

    elif choice == 2:
      name = input("Enter the video name: ")
      time = input("Enter the video time: ")
      add_videos(name, time) #10


    elif choice == 3:
      video_id = input("Enter video ID to update: ")
      name = input("Enter the video name: ")
      time = input("Enter the video time: ")
      update_video(video_id, name, time) #11


    elif choice == 4:
      video_id = input("Enter video ID to delete: ")
      delete_video(video_id) #12

    elif choice == 5:
      print("Exiting...")
      break

    else:
      print("Invalid choice!")


#6 Start program
if __name__ == "__main__":
    main()


#13 Close database AFTER main ends
conn.close()