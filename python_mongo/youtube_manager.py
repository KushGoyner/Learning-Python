# import pymongo
from pymongo import MongoClient
from bson import ObjectId

# client = pymongo.MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.kw0tl.mongodb.net/ytmanager")
client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.kw0tl.mongodb.net/ytmanager",tlsAllowInvalidCertificates=True)

db = client["ytmanager"]

video_collection = db["videos"]

def add_video(name,time):
    video_collection.insert_one({
        "name":name,
        "time":time
    })

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']} ")

def update_video(video_id,name,time):
    video_collection.update_one({
        '_id':ObjectId(video_id)
    },{"$set":
        {"name":name,
        "time":time}
    })

def delete_video(video_id):
    video_collection.delete_one({"_id":ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube Manager  | choose an option ")
        print("1. List all youtbe videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video ")
        print("5. Exit the app")
        choice = int(input("Enter your choice: "))
        

        match choice:
            case 1:
                list_videos()
            case 2:
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name,time)
            case 3:
                video_id = input("Enter video ID to update: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                update_video(video_id,name,time)
            case 4:
                video_id = input("Enter video ID to update: ")
                delete_video(video_id)
            case 5:
                break
            case _:
                print("Invalid Choice.")


if __name__ == "__main__":
    main()