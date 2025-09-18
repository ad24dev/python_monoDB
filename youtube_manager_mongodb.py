from pymongo import MongoClient
from pymongo.errors import PyMongoError, DuplicateKeyError
from bson import ObjectId

try:
  
  client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.mum3bmk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  client.admin.command("ping")
  print(" Connected to MonogoDB")
except PyMongoError as e:
  print(f" Cannot connect to MongoDB: {e}")
  raise # sto app if no DB


# choose db + collection (no try/except needed here)
db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

# --- 2. CRUD FUNCTIONS ---

def list_all_videos():
      for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")
 
    
def add_video(name, time):
    try:
     video_collection.insert_one({"name": name, "time": time})
    except DuplicateKeyError as e:
      print("Duplicate video")
    except PyMongoError as e:
      print(f" Insert failed: {e}")

def update_video(video_id, new_name, new_time):
  try:
     video_collection.update_one(
       {'_id': video_id},
       {"$set": {"name": new_name, "time": new_time}}
     )
  except PyMongoError as e:
    print(f"Update failed: {e}")
  
def delete_video(video_id):
  try:
    video_collection.delet_one({"_id": video_id})
  except PyMongoError as e:
    print(f"Delete has been failed")
 

def main():
  while True:
    print("\n Youtube manager App")
    print("1. List all videos")
    print("2. Add a new video")
    print("3. Update a video")
    print("4. Delete a video")
    print("5. Exit the app")
    choice = input("Enter your choice: ")
    
    match choice:
        case '1':
          list_all_videos()
        case "2":
          name = input("Enter the video name: ")
          time =  input("Enter the video time: ")
          add_video(name, time)
        case "3":
          video_id = input("Enter the video ID to update: ")
          name = input("Enter the video name to update: ")
          time =  input("Enter the video time to update: ")
          update_video(video_id, name, time)
        case "4":
          video_id = input("Enter the video ID to update: ")
          delete_video(video_id)
        case "5":
          break
        case _:
          print("Invalid Choice")

        

if __name__ == "__main__":
  main()
  
