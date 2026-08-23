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
  cursor.execute("SELECT * FROM videos")

  videos = cursor.fetchall()

  if not videos:
      print("\nNo videos found!")
      return

  print("\n" + "=" * 60)
  print(f"{'ID':<5} {'VIDEO NAME':<35} {'TIME':<10}")
  print("-" * 60)

  for row in videos:
      print(f"{row[0]:<5} {row[1]:<35} {row[2]:<10}")

  print("=" * 60)


#10 Add video
def add_videos(name, time):
  if not name.strip() or not time.strip():
    print("\nVideo name and time cannot be empty!")
    return

  try:
    cursor.execute(
      "INSERT INTO videos (name, time) VALUES (?, ?)",
      (name, time)
    )
    conn.commit()

    print("\nVideo added successfully!")

  except sqlite3.Error as e:
    print(f"\nDatabase error: {e}")


#11 Update video
def update_video(video_id, new_name, new_time):
  if not new_name.strip() or not new_time.strip():
    print("\n Video name and time cannot be empty!")
    return

  cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
  conn.commit()

  if cursor.rowcount == 0:
    print("Video ID not found!")
  else:
    print("\nVideo updated successfully!")


#12 Delete video
def delete_video(video_id):
  cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
  conn.commit()

  if cursor.rowcount == 0:
    print("\n Video ID not found!")
  else:
    print("\n Video deleted successfully!")


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

    try:
      choice = int(input("Enter your choice: "))

    except ValueError:
      print("\n Please enter a valid number!")
      continue

    #8 User choice
    if choice == 1:
     list_videos() #9

    elif choice == 2:
      name = input("Enter the video name: ")
      time = input("Enter the video time: ")
      add_videos(name, time) #10


    elif choice == 3:
      try:
        video_id = int(input("Enter video ID to update: "))

      except ValueError:
        print("\n Please enter a valid video ID!")
        continue

      name = input("Enter the video name: ")
      time = input("Enter the video time: ")
      update_video(video_id, name, time) #11


    elif choice == 4:
      try:
        video_id = int(input("Enter video ID to delete: "))

      except ValueError:
        print("\n Please enter a valid video ID!")
        continue

      delete_video(video_id) #12

    elif choice == 5:
      print("Exiting...")
      break

    else:
      print("Invalid choice!!")


#6 Start program
if __name__ == "__main__":
    main()


#13 Close database AFTER main ends
conn.close()


